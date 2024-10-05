from extras.plugins import PluginConfig
import netbox.dcim.models.devices

class NetBoxAssetTagBeGoneConfig(PluginConfig):
    name = 'netbox_asset_tag_be_gone'
    verbose_name = 'NetBox Asset Tag Be Gone'
    description = 'Simply disable adding the Asset Tag to device names'
    version = '0.1'
    base_url = 'asset-be-gone'


config = NetBoxAssetTagBeGoneConfig

devices.Device.__str__ = lambda self: f'{self.name}'