import os
import time
import types
import inspect
import logging
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from SAF.driver.appium_driver import AppiumDriver
from abc import ABCMeta

def find_all_none_flow_methods(_class):
    return [func for _cls in inspect.getmro(_class)[:-1] if (not hasattr(_cls, "flow_name") or _cls.flow_name is None) and (not hasattr(_cls, "project") or _cls.project is None) for func in dir(_cls) if callable(getattr(_cls, func))]

def find_context_for_method_name(_class, method_name):
    _class_definition = _class.__class__
    #Check first if the class have a context defined
    instance_context = getattr(_class, "context", None)
    #Check if class definition overloaded this context
    class_list = inspect.getmro(_class_definition)
    for _cls in class_list:
        if method_name in [key for key, value in _cls.__dict__.items() if type(value) == types.FunctionType]: 
            definition_context = getattr(_cls, "context", None)
            break

    if definition_context is None:
        if instance_context is None:
            #If no defined context nor instance context default is "NATIVE_APP"
            return "NATIVE_APP"
        else:
            #If no context is defined in the class use the context in the instance
            return instance_context
    else:
        #If context is defined in the class use that one
        return definition_context

class BaseFlow(object):
    __metaclass__ = ABCMeta
    """
    Flow meta data:
    system: Mark the platfrom that the flow belongs in (one layer down)
    project: Mark the project of the flow (parent should be platform, two layers down)
    flow_name: Mark the specific flow of the project of the specific platform (parent should be project, three layers down)
    folder_name: To manipulate the UIMap directory to be able to put UI maps in sub folders (same layer as actual flow class)
    """
    system = None
    project = None
    flow_name = None
    folder_name = None

    base_path = "/resources/ui_map/"
    logging_ignore_methods = ["load_ui_map"]
    func_ignore_methods = []
    def __init__(self, driver):
        """
        :type driver: AppiumDriver
        :param driver:
        """
        self.driver = driver
        self.wdvr = driver.wdvr
        self.func_ignore_methods = find_all_none_flow_methods(self.__class__)

        self.ui_map = self.load_ui_map(system=self.system, project=self.project, flow_name=self.flow_name, folder_name=self.folder_name)
        self.driver.load_ui_map(self.project,self.flow_name, self.ui_map)

    def __getattribute__(self, attr):
        method = object.__getattribute__(self, attr)

        #except AttributeError:
        #    raise NameError("NameError: name '%s' is not defined" % attr)
        if type(method) == types.MethodType:
            if attr in self.func_ignore_methods:
                self.driver.current_project = self.project
                self.driver.current_flow = self.flow_name
                return method
                
            elif not inspect.isabstract(self) and callable(method):
                if self.driver.driver_class == "appium":
                    #If the flow have no context variable it is defaulted to always run NATIVE_APP. 
                    context = find_context_for_method_name(self, attr)# getattr(self, "context", "NATIVE_APP")
                    url = getattr(self, "url", None)
                    #Context can be an index so it could be type int
                    if type(context) == int:
                        self.driver.switch_to_webview(webview_index=context)
                    #If context isn't type int it should be type str which is the webview's name
                    elif type(context) == str:
                        self.driver.switch_to_webview(webview_name=context)
                    
                    elif type(context) == dict:
                        if list(context.keys())[0] == "url":
                            self.driver.switch_to_webview(webview_url=context.get('url'))
                        elif list(context.keys())[0] == "title":
                            self.driver.switch_to_webview(webview_title=context.get('title'))

                    if url is not None:
                        self.driver.switch_to_window(url)

                if self.driver.driver_class == "selenium" and hasattr(self, "wn"):
                    self.driver.switch_window(self.wn)
                self.driver.current_project = self.project
                self.driver.current_flow = self.flow_name
                if method.__name__ not in self.logging_ignore_methods:
                    logging.info("START - {}".format(method.__name__))
        return method

    def load_ui_map(self, system=None, project=None, flow_name = None, folder_name=None):
        sys = self.system if system is None else system.lower()
        proj = self.project if project is None else project.lower()
        fn = self.flow_name if flow_name is None else flow_name.lower()

        if fn is None:
            raise IOError("flow_name cannot be none")
        
        path = self.base_path + sys + '/' + proj + "/"
        if folder_name is not None:
            path += folder_name + "/"
        path += fn + ".json"

        ui_map_path = ma_misc.get_abs_path(path)
        ui_map = saf_misc.load_json(ui_map_path)
        return ui_map

    def change_page(self):
        self.driver.session_data["current_flow"] = self.flow_name

    def get_text_from_str_id(self, object_name):
        old_flow = None
        if self.driver.session_data["current_flow"] != self.flow_name:
            old_flow = self.driver.session_data["current_flow"]
            self.driver.session_data["current_flow"] = self.flow_name

        obj = self.driver.get_ui_obj_dict(object_name)
        
        if old_flow is not None:
            self.driver.session_data["current_flow"] = old_flow

        if not obj["locator"].get("str_id", False):
            raise KeyError("UI flow: " + self.flow_name + " object: " + object_name + " does not have str_id locator")
        else:
            return_str = self.driver.session_data["app_strings"][self.project][obj["locator"]["str_id"]]
            if return_str.startswith('\"') and return_str.endswith('\"'):
                return return_str[1:-1]
            else:
                return return_str

    def switch_to_webview(self, webview):
        self.driver.switch_to_webview(webview)