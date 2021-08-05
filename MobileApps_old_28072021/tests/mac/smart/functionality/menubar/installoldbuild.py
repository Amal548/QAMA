import pexpect


class Install_old_build():
    
    def uninstall_latest_build(self):
        ch=pexpect.spawn('sudo rm -r -f /Applications/HP\ Smart.app ')
        ch.expect('Password:')
        ch.sendline('Spytester123')
        
    def install_old_build(self):
        ch=pexpect.spawn('sudo installer -pkg /Users/itest/Desktop/HP\ Smart-3.0.203.pkg -target / ')
        ch.expect('Password:')
        ch.sendline('Spytester123')
            

if __name__=='__main__':
    run=Install_old_build()
    res=run.uninstall_latest_build()
    