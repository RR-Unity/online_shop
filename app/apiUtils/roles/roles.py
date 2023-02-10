OBJECTS_READ = 'objects.read'
OBJECTS_LOCATIONS_READ = 'objects.locations.read'
OBJECTS_CREATE = 'objects.create'
OBJECTS_UPDATE = 'objects.update'
OBJECTS_STATUS_UPDATE = 'objects.status.update'
OBJECTS_IMAGE_UPDATE = 'objects.image.update'
OBJECTS_DELETE = 'objects.delete'


LOCATIONS_READ = 'locations.read'
LOCATIONS_CREATE = 'locations.create'
LOCATIONS_UPDATE = 'locations.update'
LOCATIONS_STATUS_UPDATE = 'locations.status.update'
LOCATIONS_IMAGE_UPLOAD = 'locations.image.update'
LOCATIONS_DELETE = 'locations.delete'


COMPANIES_READ = 'companies.read'
COMPANIES_CREATE = 'companies.create'
COMPANIES_UPDATE = 'companies.update'
COMPANIES_STATUS_UPDATE = 'companies.status.update'
COMPANIES_IMAGE_UPLOAD = 'companies.image.update'
COMPANIES_DELETE = 'companies.delete'


USERS_READ = 'users.read'
USERS_CREATE = 'users.create'
USERS_UPDATE = 'users.update'
USERS_STATUS_UPDATE = 'users.status.update'
USERS_DELETE = 'users.delete'


ZONES_READ = 'zones.read'
ZONES_CREATE = 'zones.create'
ZONES_UPDATE = 'zones.update'
ZONES_DELETE = 'zones.delete'
ZONES_STATUS_UPDATE = 'zones.status.update'
ZONES_LINK_LOCATION = 'zones.location.link'
ZONES_UNLINK_LOCATION = 'zones.location.unlink'
ZONES_IMAGE_MANAGE = 'zones.image.manage'

ZONES_AGENT_SETUPS_READ = 'zones_agent_setups.read'
ZONES_AGENT_SETUPS_UPDATE = 'zones_agent_setups.update'
ZONES_AGENT_SETUPS_IMAGE_MANAGE = 'zones_agent_setups.agent_image.manage'


ZONE_MAP_READ = 'zone.map.read'
ZONE_MAP_CREATE = 'zone.map.create'
ZONE_MAP_UPDATE = 'zone.map.update'
ZONE_MAP_DELETE = 'zone.map.delete'


CONTENTS_READ = 'contents.read'
CONTENTS_UPDATE = 'contents.update'
CONTENTS_STATUS_UPDATE = 'contents.status.update'
CONTENTS_DELETE = 'contents.delete'

CONTENT_SETS_READ = 'content_sets.read'
CONTENT_SETS_CREATE = 'content_sets.create'
CONTENT_SETS_UPLOAD = 'content_sets.upload'

AGENT_CONTENT_SET_READ = 'agent.content_set.read'
AGENT_CONTENT_SET_CREATE = 'agent.content_set.create'
AGENT_CONTENT_SETS_UPLOAD = 'agent.content_sets.upload'

CLIENTS_READ = 'clients.read'
CLIENTS_CREATE = 'clients.create'
CLIENTS_UPDATE = 'clients.update'
CLIENTS_STATUS_UPDATE = 'clients.status.update'
CLIENTS_DELETE = 'clients.delete'

ROLE_GROUP_READ = 'role.group.read'
ROLE_GROUP_CREATE = 'role.group.create'
ROLE_GROUP_UPDATE = 'role.group.update'
ROLE_GROUP_DELETE = 'role.group.delete'

USER_PERMIT_GROUP_READ = 'user.permit.group.read'
USER_PERMIT_GROUP_CREATE = 'user.permit.group.create'
USER_PERMIT_GROUP_UPDATE = 'user.permit.group.update'
USER_PERMIT_GROUP_DELETE = 'user.permit.group.delete'


variables = dir()   # noqa: WPS110


def get_roles():
    return [eval(name) for name in variables if name.isupper() and not name.startswith('_')]  # noqa: WPS110, S307
