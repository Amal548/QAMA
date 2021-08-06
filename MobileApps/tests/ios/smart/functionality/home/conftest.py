import pytest
from MobileApps.resources.const.ios.const import HOME_TILES as ht
  
@pytest.fixture
def setup_default_tiles():
    return [
       ht.TILE_INSTANT_INK, ht.TILE_PLAY_LEARN, ht.TILE_SMART_TASK,
       ht.TILE_CAMERA_SCAN, ht.TILE_HELP_AND_SUPPORT, ht.TILE_PRINT_PHOTOS,
       ht.TILE_PRINT_DOCUMENTS, ht.TILE_SCAN, ht.TILE_COPY, ht.TILE_CREATE_PHOTOS
    ]
