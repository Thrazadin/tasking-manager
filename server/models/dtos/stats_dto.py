from schematics import Model
from schematics.types import StringType, IntType, BooleanType
from schematics.types.compound import ListType, ModelType
from server.models.dtos.mapping_dto import TaskHistoryDTO


class UserContribution(Model):
    """ User contribution for a project """
    username = StringType()
    mapped = IntType()
    validated = IntType()


class ProjectContributionsDTO(Model):
    """ DTO for all user contributons on a project """
    def __init__(self):
        super().__init__()
        self.user_contributions = []

    user_contributions = ListType(ModelType(UserContribution), serialized_name='userContributions')


class Pagination(Model):
    """ Properties for paginating results """
    def __init__(self, paginated_result):
        """ Instantiate from a Flask-SQLAlchemy paginated result"""
        super().__init__()

        self.has_next = paginated_result.has_next
        self.has_prev = paginated_result.has_prev
        self.next_num = paginated_result.next_num
        self.page = paginated_result.page
        self.pages = paginated_result.pages
        self.prev_num = paginated_result.prev_num
        self.per_page = paginated_result.per_page
        self.total = paginated_result.total

    has_next = BooleanType(serialized_name='hasNext')
    has_prev = BooleanType(serialized_name='hasPrev')
    next_num = IntType(serialized_name='nextNum')
    page = IntType()
    pages = IntType()
    prev_num = IntType(serialized_name='prevNum')
    per_page = IntType(serialized_name='perPage')
    total = IntType()


class ProjectActivityDTO(Model):
    """ DTO to hold all project activity """
    def __init__(self):
        super().__init__()
        self.activity = []

    pagination = ModelType(Pagination)
    activity = ListType(ModelType(TaskHistoryDTO))


class HomePageStatsDTO(Model):
    """ DTO for stats we want to display on the homepage """
    mappers_online = IntType(serialized_name='mappersOnline')
    tasks_mapped = IntType(serialized_name='tasksMapped')
    total_mappers = IntType(serialized_name='totalMappers')
