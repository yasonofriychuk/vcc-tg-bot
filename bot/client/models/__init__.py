"""Contains all the data models used in inputs/outputs"""

from .body_ldap_login_auth_ldap_login_post import BodyLdapLoginAuthLdapLoginPost
from .body_ldap_login_auth_ldap_login_post_fingerprint import BodyLdapLoginAuthLdapLoginPostFingerprint
from .body_login_auth_login_post import BodyLoginAuthLoginPost
from .body_login_auth_login_post_fingerprint import BodyLoginAuthLoginPostFingerprint
from .body_upload_file_meetings_attachments_post import BodyUploadFileMeetingsAttachmentsPost
from .building_bare import BuildingBare
from .building_create import BuildingCreate
from .building_full import BuildingFull
from .building_list import BuildingList
from .catalog_element_bare import CatalogElementBare
from .catalog_element_create import CatalogElementCreate
from .cisco_participants_limit_out import CiscoParticipantsLimitOut
from .cisco_room_bare import CiscoRoomBare
from .cisco_room_public_bare import CiscoRoomPublicBare
from .cisco_vcs_setting_bare import CiscoVCSSettingBare
from .cisco_vcs_setting_create import CiscoVCSSettingCreate
from .create_user_in import CreateUserIn
from .cumulative_meeting import CumulativeMeeting
from .cumulative_meetings import CumulativeMeetings
from .cumulative_type import CumulativeType
from .department_bare import DepartmentBare
from .department_brief import DepartmentBrief
from .department_full import DepartmentFull
from .department_list import DepartmentList
from .department_list_brief import DepartmentListBrief
from .department_update import DepartmentUpdate
from .email_template_editable_fields import EmailTemplateEditableFields
from .email_template_list import EmailTemplateList
from .email_template_out import EmailTemplateOut
from .event_bare import EventBare
from .event_create import EventCreate
from .event_full import EventFull
from .event_list import EventList
from .event_relative_stat import EventRelativeStat
from .event_short import EventShort
from .event_time_collision import EventTimeCollision
from .external_vcs_setting_create import ExternalVCSSettingCreate
from .external_vcs_setting_out import ExternalVCSSettingOut
from .file_bare import FileBare
from .file_create import FileCreate
from .file_full import FileFull
from .group_bare import GroupBare
from .group_bare_params import GroupBareParams
from .group_create import GroupCreate
from .group_create_params import GroupCreateParams
from .group_full import GroupFull
from .group_full_params import GroupFullParams
from .group_list import GroupList
from .group_share_token import GroupShareToken
from .group_update import GroupUpdate
from .group_update_params import GroupUpdateParams
from .http_validation_error import HTTPValidationError
from .id_mixin import IdMixin
from .login_out import LoginOut
from .login_out_tutorials_progress import LoginOutTutorialsProgress
from .meeting_backend import MeetingBackend
from .meeting_bare import MeetingBare
from .meeting_create_validated import MeetingCreateValidated
from .meeting_full import MeetingFull
from .meeting_license import MeetingLicense
from .meeting_license_list import MeetingLicenseList
from .meeting_license_threshold import MeetingLicenseThreshold
from .meeting_license_used_time import MeetingLicenseUsedTime
from .meeting_license_used_time_list import MeetingLicenseUsedTimeList
from .meeting_list import MeetingList
from .meeting_permalink_organizer_full import MeetingPermalinkOrganizerFull
from .meeting_permalink_out import MeetingPermalinkOut
from .meeting_recurrence_brief import MeetingRecurrenceBrief
from .meeting_recurrence_create import MeetingRecurrenceCreate
from .meeting_recurrence_frequency import MeetingRecurrenceFrequency
from .meeting_recurrence_update_type import MeetingRecurrenceUpdateType
from .meeting_recurrence_weekday import MeetingRecurrenceWeekday
from .meeting_short import MeetingShort
from .meeting_short_extended import MeetingShortExtended
from .meeting_sorting_fields import MeetingSortingFields
from .meeting_stat_list import MeetingStatList
from .meeting_states import MeetingStates
from .meeting_time_stat import MeetingTimeStat
from .meeting_update_validated import MeetingUpdateValidated
from .meetings_calendar_list import MeetingsCalendarList
from .meetings_traffic import MeetingsTraffic
from .municipal_area_list import MunicipalAreaList
from .participant_create import ParticipantCreate
from .participant_involved import ParticipantInvolved
from .participant_mock import ParticipantMock
from .participant_out import ParticipantOut
from .participants_collision_in import ParticipantsCollisionIn
from .participants_collision_out import ParticipantsCollisionOut
from .permanent_room_in import PermanentRoomIn
from .permanent_room_list import PermanentRoomList
from .permanent_room_out import PermanentRoomOut
from .private_license_in import PrivateLicenseIn
from .private_license_list import PrivateLicenseList
from .private_license_out import PrivateLicenseOut
from .refresh_token_in import RefreshTokenIn
from .register_user_in import RegisterUserIn
from .report_by_date import ReportByDate
from .report_type import ReportType
from .reset_password_confirm import ResetPasswordConfirm
from .reset_password_in import ResetPasswordIn
from .role_bare import RoleBare
from .role_list import RoleList
from .room_bare import RoomBare
from .room_create import RoomCreate
from .room_full import RoomFull
from .room_list import RoomList
from .room_short import RoomShort
from .room_stat import RoomStat
from .room_stat_list import RoomStatList
from .setting_update import SettingUpdate
from .simple_user_bare import SimpleUserBare
from .simple_user_create import SimpleUserCreate
from .simple_user_list import SimpleUserList
from .status_response import StatusResponse
from .status_response_warning_info_item import StatusResponseWarningInfoItem
from .template_variable_description_out import TemplateVariableDescriptionOut
from .time_system import TimeSystem
from .top_by_organized_departments import TopByOrganizedDepartments
from .top_by_organized_user import TopByOrganizedUser
from .user_brief import UserBrief
from .user_info_out import UserInfoOut
from .user_list_brief import UserListBrief
from .user_list_out import UserListOut
from .user_meetings import UserMeetings
from .user_meetings_list import UserMeetingsList
from .user_out import UserOut
from .user_out_full import UserOutFull
from .user_out_full_brief_role import UserOutFullBriefRole
from .user_priority import UserPriority
from .user_self_update_info import UserSelfUpdateInfo
from .user_tutorial_mark import UserTutorialMark
from .user_tutorials import UserTutorials
from .user_update_in import UserUpdateIn
from .validation_error import ValidationError
from .video_description import VideoDescription
from .video_description_list import VideoDescriptionList
from .vinteo_fps import VinteoFPS
from .vinteo_global_setting_update import VinteoGlobalSettingUpdate
from .vinteo_participants_limit_out import VinteoParticipantsLimitOut
from .vinteo_resolutions import VinteoResolutions
from .vinteo_room_bare import VinteoRoomBare
from .vinteo_room_public_bare import VinteoRoomPublicBare
from .vinteo_vcs_setting_bare import VinteoVCSSettingBare
from .vinteo_vcs_setting_create import VinteoVCSSettingCreate

__all__ = (
    "BodyLdapLoginAuthLdapLoginPost",
    "BodyLdapLoginAuthLdapLoginPostFingerprint",
    "BodyLoginAuthLoginPost",
    "BodyLoginAuthLoginPostFingerprint",
    "BodyUploadFileMeetingsAttachmentsPost",
    "BuildingBare",
    "BuildingCreate",
    "BuildingFull",
    "BuildingList",
    "CatalogElementBare",
    "CatalogElementCreate",
    "CiscoParticipantsLimitOut",
    "CiscoRoomBare",
    "CiscoRoomPublicBare",
    "CiscoVCSSettingBare",
    "CiscoVCSSettingCreate",
    "CreateUserIn",
    "CumulativeMeeting",
    "CumulativeMeetings",
    "CumulativeType",
    "DepartmentBare",
    "DepartmentBrief",
    "DepartmentFull",
    "DepartmentList",
    "DepartmentListBrief",
    "DepartmentUpdate",
    "EmailTemplateEditableFields",
    "EmailTemplateList",
    "EmailTemplateOut",
    "EventBare",
    "EventCreate",
    "EventFull",
    "EventList",
    "EventRelativeStat",
    "EventShort",
    "EventTimeCollision",
    "ExternalVCSSettingCreate",
    "ExternalVCSSettingOut",
    "FileBare",
    "FileCreate",
    "FileFull",
    "GroupBare",
    "GroupBareParams",
    "GroupCreate",
    "GroupCreateParams",
    "GroupFull",
    "GroupFullParams",
    "GroupList",
    "GroupShareToken",
    "GroupUpdate",
    "GroupUpdateParams",
    "HTTPValidationError",
    "IdMixin",
    "LoginOut",
    "LoginOutTutorialsProgress",
    "MeetingBackend",
    "MeetingBare",
    "MeetingCreateValidated",
    "MeetingFull",
    "MeetingLicense",
    "MeetingLicenseList",
    "MeetingLicenseThreshold",
    "MeetingLicenseUsedTime",
    "MeetingLicenseUsedTimeList",
    "MeetingList",
    "MeetingPermalinkOrganizerFull",
    "MeetingPermalinkOut",
    "MeetingRecurrenceBrief",
    "MeetingRecurrenceCreate",
    "MeetingRecurrenceFrequency",
    "MeetingRecurrenceUpdateType",
    "MeetingRecurrenceWeekday",
    "MeetingsCalendarList",
    "MeetingShort",
    "MeetingShortExtended",
    "MeetingSortingFields",
    "MeetingStates",
    "MeetingStatList",
    "MeetingsTraffic",
    "MeetingTimeStat",
    "MeetingUpdateValidated",
    "MunicipalAreaList",
    "ParticipantCreate",
    "ParticipantInvolved",
    "ParticipantMock",
    "ParticipantOut",
    "ParticipantsCollisionIn",
    "ParticipantsCollisionOut",
    "PermanentRoomIn",
    "PermanentRoomList",
    "PermanentRoomOut",
    "PrivateLicenseIn",
    "PrivateLicenseList",
    "PrivateLicenseOut",
    "RefreshTokenIn",
    "RegisterUserIn",
    "ReportByDate",
    "ReportType",
    "ResetPasswordConfirm",
    "ResetPasswordIn",
    "RoleBare",
    "RoleList",
    "RoomBare",
    "RoomCreate",
    "RoomFull",
    "RoomList",
    "RoomShort",
    "RoomStat",
    "RoomStatList",
    "SettingUpdate",
    "SimpleUserBare",
    "SimpleUserCreate",
    "SimpleUserList",
    "StatusResponse",
    "StatusResponseWarningInfoItem",
    "TemplateVariableDescriptionOut",
    "TimeSystem",
    "TopByOrganizedDepartments",
    "TopByOrganizedUser",
    "UserBrief",
    "UserInfoOut",
    "UserListBrief",
    "UserListOut",
    "UserMeetings",
    "UserMeetingsList",
    "UserOut",
    "UserOutFull",
    "UserOutFullBriefRole",
    "UserPriority",
    "UserSelfUpdateInfo",
    "UserTutorialMark",
    "UserTutorials",
    "UserUpdateIn",
    "ValidationError",
    "VideoDescription",
    "VideoDescriptionList",
    "VinteoFPS",
    "VinteoGlobalSettingUpdate",
    "VinteoParticipantsLimitOut",
    "VinteoResolutions",
    "VinteoRoomBare",
    "VinteoRoomPublicBare",
    "VinteoVCSSettingBare",
    "VinteoVCSSettingCreate",
)
