# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabasePlanDirective(object):
    """
    Manage resource allocations among databases. Besides name, need to have at least one other property.
    """

    #: A constant which can be used with the type property of a DatabasePlanDirective.
    #: This constant has a value of "DATABASE"
    TYPE_DATABASE = "DATABASE"

    #: A constant which can be used with the type property of a DatabasePlanDirective.
    #: This constant has a value of "PROFILE"
    TYPE_PROFILE = "PROFILE"

    #: A constant which can be used with the type property of a DatabasePlanDirective.
    #: This constant has a value of "OTHER"
    TYPE_OTHER = "OTHER"

    #: A constant which can be used with the role property of a DatabasePlanDirective.
    #: This constant has a value of "PRIMARY"
    ROLE_PRIMARY = "PRIMARY"

    #: A constant which can be used with the role property of a DatabasePlanDirective.
    #: This constant has a value of "STANDBY"
    ROLE_STANDBY = "STANDBY"

    #: A constant which can be used with the role property of a DatabasePlanDirective.
    #: This constant has a value of "NONE"
    ROLE_NONE = "NONE"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabasePlanDirective object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this DatabasePlanDirective.
        :type name: str

        :param share:
            The value to assign to the share property of this DatabasePlanDirective.
        :type share: int

        :param level:
            The value to assign to the level property of this DatabasePlanDirective.
        :type level: int

        :param allocation:
            The value to assign to the allocation property of this DatabasePlanDirective.
        :type allocation: int

        :param limit:
            The value to assign to the limit property of this DatabasePlanDirective.
        :type limit: int

        :param is_flash_cache_on:
            The value to assign to the is_flash_cache_on property of this DatabasePlanDirective.
        :type is_flash_cache_on: bool

        :param is_pmem_cache_on:
            The value to assign to the is_pmem_cache_on property of this DatabasePlanDirective.
        :type is_pmem_cache_on: bool

        :param is_flash_log_on:
            The value to assign to the is_flash_log_on property of this DatabasePlanDirective.
        :type is_flash_log_on: bool

        :param is_pmem_log_on:
            The value to assign to the is_pmem_log_on property of this DatabasePlanDirective.
        :type is_pmem_log_on: bool

        :param flash_cache_limit:
            The value to assign to the flash_cache_limit property of this DatabasePlanDirective.
        :type flash_cache_limit: str

        :param flash_cache_min:
            The value to assign to the flash_cache_min property of this DatabasePlanDirective.
        :type flash_cache_min: str

        :param flash_cache_size:
            The value to assign to the flash_cache_size property of this DatabasePlanDirective.
        :type flash_cache_size: str

        :param pmem_cache_limit:
            The value to assign to the pmem_cache_limit property of this DatabasePlanDirective.
        :type pmem_cache_limit: str

        :param pmem_cache_min:
            The value to assign to the pmem_cache_min property of this DatabasePlanDirective.
        :type pmem_cache_min: str

        :param pmem_cache_size:
            The value to assign to the pmem_cache_size property of this DatabasePlanDirective.
        :type pmem_cache_size: str

        :param asm_cluster:
            The value to assign to the asm_cluster property of this DatabasePlanDirective.
        :type asm_cluster: str

        :param type:
            The value to assign to the type property of this DatabasePlanDirective.
            Allowed values for this property are: "DATABASE", "PROFILE", "OTHER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param role:
            The value to assign to the role property of this DatabasePlanDirective.
            Allowed values for this property are: "PRIMARY", "STANDBY", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type role: str

        """
        self.swagger_types = {
            'name': 'str',
            'share': 'int',
            'level': 'int',
            'allocation': 'int',
            'limit': 'int',
            'is_flash_cache_on': 'bool',
            'is_pmem_cache_on': 'bool',
            'is_flash_log_on': 'bool',
            'is_pmem_log_on': 'bool',
            'flash_cache_limit': 'str',
            'flash_cache_min': 'str',
            'flash_cache_size': 'str',
            'pmem_cache_limit': 'str',
            'pmem_cache_min': 'str',
            'pmem_cache_size': 'str',
            'asm_cluster': 'str',
            'type': 'str',
            'role': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'share': 'share',
            'level': 'level',
            'allocation': 'allocation',
            'limit': 'limit',
            'is_flash_cache_on': 'isFlashCacheOn',
            'is_pmem_cache_on': 'isPmemCacheOn',
            'is_flash_log_on': 'isFlashLogOn',
            'is_pmem_log_on': 'isPmemLogOn',
            'flash_cache_limit': 'flashCacheLimit',
            'flash_cache_min': 'flashCacheMin',
            'flash_cache_size': 'flashCacheSize',
            'pmem_cache_limit': 'pmemCacheLimit',
            'pmem_cache_min': 'pmemCacheMin',
            'pmem_cache_size': 'pmemCacheSize',
            'asm_cluster': 'asmCluster',
            'type': 'type',
            'role': 'role'
        }

        self._name = None
        self._share = None
        self._level = None
        self._allocation = None
        self._limit = None
        self._is_flash_cache_on = None
        self._is_pmem_cache_on = None
        self._is_flash_log_on = None
        self._is_pmem_log_on = None
        self._flash_cache_limit = None
        self._flash_cache_min = None
        self._flash_cache_size = None
        self._pmem_cache_limit = None
        self._pmem_cache_min = None
        self._pmem_cache_size = None
        self._asm_cluster = None
        self._type = None
        self._role = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this DatabasePlanDirective.
        The name of a database or a profile.


        :return: The name of this DatabasePlanDirective.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DatabasePlanDirective.
        The name of a database or a profile.


        :param name: The name of this DatabasePlanDirective.
        :type: str
        """
        self._name = name

    @property
    def share(self):
        """
        Gets the share of this DatabasePlanDirective.
        The relative priority a database in the database plan. A higher share value implies
        higher priority and more access to the I/O resources.
        Use either share or (level, allocation). All plan directives in a database plan
        should use the same setting.
        Share-based resource allocation is the recommended method for a database plan.


        :return: The share of this DatabasePlanDirective.
        :rtype: int
        """
        return self._share

    @share.setter
    def share(self, share):
        """
        Sets the share of this DatabasePlanDirective.
        The relative priority a database in the database plan. A higher share value implies
        higher priority and more access to the I/O resources.
        Use either share or (level, allocation). All plan directives in a database plan
        should use the same setting.
        Share-based resource allocation is the recommended method for a database plan.


        :param share: The share of this DatabasePlanDirective.
        :type: int
        """
        self._share = share

    @property
    def level(self):
        """
        Gets the level of this DatabasePlanDirective.
        The allocation level. Valid values are from 1 to 8. Resources are allocated to level 1 first,
        and then remaining resources are allocated to level 2, and so on.


        :return: The level of this DatabasePlanDirective.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """
        Sets the level of this DatabasePlanDirective.
        The allocation level. Valid values are from 1 to 8. Resources are allocated to level 1 first,
        and then remaining resources are allocated to level 2, and so on.


        :param level: The level of this DatabasePlanDirective.
        :type: int
        """
        self._level = level

    @property
    def allocation(self):
        """
        Gets the allocation of this DatabasePlanDirective.
        The resource allocation as a percentage (0-100) within the level.


        :return: The allocation of this DatabasePlanDirective.
        :rtype: int
        """
        return self._allocation

    @allocation.setter
    def allocation(self, allocation):
        """
        Sets the allocation of this DatabasePlanDirective.
        The resource allocation as a percentage (0-100) within the level.


        :param allocation: The allocation of this DatabasePlanDirective.
        :type: int
        """
        self._allocation = allocation

    @property
    def limit(self):
        """
        Gets the limit of this DatabasePlanDirective.
        The maximum I/O utilization limit as a percentage of the available resources.


        :return: The limit of this DatabasePlanDirective.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this DatabasePlanDirective.
        The maximum I/O utilization limit as a percentage of the available resources.


        :param limit: The limit of this DatabasePlanDirective.
        :type: int
        """
        self._limit = limit

    @property
    def is_flash_cache_on(self):
        """
        Gets the is_flash_cache_on of this DatabasePlanDirective.
        Controls use of Exadata Smart Flash Cache by a database.
        This ensures that cache space is reserved for mission-critical databases.
        flashcache=off is invalid in a directive that contains the flashcachemin, flashcachelimit, or flashcachesize attributes.


        :return: The is_flash_cache_on of this DatabasePlanDirective.
        :rtype: bool
        """
        return self._is_flash_cache_on

    @is_flash_cache_on.setter
    def is_flash_cache_on(self, is_flash_cache_on):
        """
        Sets the is_flash_cache_on of this DatabasePlanDirective.
        Controls use of Exadata Smart Flash Cache by a database.
        This ensures that cache space is reserved for mission-critical databases.
        flashcache=off is invalid in a directive that contains the flashcachemin, flashcachelimit, or flashcachesize attributes.


        :param is_flash_cache_on: The is_flash_cache_on of this DatabasePlanDirective.
        :type: bool
        """
        self._is_flash_cache_on = is_flash_cache_on

    @property
    def is_pmem_cache_on(self):
        """
        Gets the is_pmem_cache_on of this DatabasePlanDirective.
        Controls use of the persistent memory (PMEM) cache by a database. This ensures that cache space
        is reserved for mission-critical databases.
        pmemcache=off is invalid in a directive that contains the pmemcachemin, pmemcachelimit, or pmemcachesize attributes.


        :return: The is_pmem_cache_on of this DatabasePlanDirective.
        :rtype: bool
        """
        return self._is_pmem_cache_on

    @is_pmem_cache_on.setter
    def is_pmem_cache_on(self, is_pmem_cache_on):
        """
        Sets the is_pmem_cache_on of this DatabasePlanDirective.
        Controls use of the persistent memory (PMEM) cache by a database. This ensures that cache space
        is reserved for mission-critical databases.
        pmemcache=off is invalid in a directive that contains the pmemcachemin, pmemcachelimit, or pmemcachesize attributes.


        :param is_pmem_cache_on: The is_pmem_cache_on of this DatabasePlanDirective.
        :type: bool
        """
        self._is_pmem_cache_on = is_pmem_cache_on

    @property
    def is_flash_log_on(self):
        """
        Gets the is_flash_log_on of this DatabasePlanDirective.
        Controls use of Exadata Smart Flash Log by a database.
        This ensures that Exadata Smart Flash Log is reserved for mission-critical databases.


        :return: The is_flash_log_on of this DatabasePlanDirective.
        :rtype: bool
        """
        return self._is_flash_log_on

    @is_flash_log_on.setter
    def is_flash_log_on(self, is_flash_log_on):
        """
        Sets the is_flash_log_on of this DatabasePlanDirective.
        Controls use of Exadata Smart Flash Log by a database.
        This ensures that Exadata Smart Flash Log is reserved for mission-critical databases.


        :param is_flash_log_on: The is_flash_log_on of this DatabasePlanDirective.
        :type: bool
        """
        self._is_flash_log_on = is_flash_log_on

    @property
    def is_pmem_log_on(self):
        """
        Gets the is_pmem_log_on of this DatabasePlanDirective.
        Controls use of persistent memory logging (PMEM log) by a database.
        This ensures that PMEM log is reserved for mission-critical databases.


        :return: The is_pmem_log_on of this DatabasePlanDirective.
        :rtype: bool
        """
        return self._is_pmem_log_on

    @is_pmem_log_on.setter
    def is_pmem_log_on(self, is_pmem_log_on):
        """
        Sets the is_pmem_log_on of this DatabasePlanDirective.
        Controls use of persistent memory logging (PMEM log) by a database.
        This ensures that PMEM log is reserved for mission-critical databases.


        :param is_pmem_log_on: The is_pmem_log_on of this DatabasePlanDirective.
        :type: bool
        """
        self._is_pmem_log_on = is_pmem_log_on

    @property
    def flash_cache_limit(self):
        """
        Gets the flash_cache_limit of this DatabasePlanDirective.
        Defines a soft limit for space usage in Exadata Smart Flash Cache.
        If the cache is not full, the limit can be exceeded.
        You specify the value for flashcachelimit in bytes. You can also use the suffixes M (megabytes),
        G (gigabytes), or T (terabytes) to specify larger values. For example, 300M, 150G, or 1T.
        The value for flashcachelimit must be at least 4 MB.
        The flashcachelimit and flashcachesize attributes cannot be specified in the same directive.
        The value for flashcachelimit cannot be smaller than flashcachemin, if it is specified.


        :return: The flash_cache_limit of this DatabasePlanDirective.
        :rtype: str
        """
        return self._flash_cache_limit

    @flash_cache_limit.setter
    def flash_cache_limit(self, flash_cache_limit):
        """
        Sets the flash_cache_limit of this DatabasePlanDirective.
        Defines a soft limit for space usage in Exadata Smart Flash Cache.
        If the cache is not full, the limit can be exceeded.
        You specify the value for flashcachelimit in bytes. You can also use the suffixes M (megabytes),
        G (gigabytes), or T (terabytes) to specify larger values. For example, 300M, 150G, or 1T.
        The value for flashcachelimit must be at least 4 MB.
        The flashcachelimit and flashcachesize attributes cannot be specified in the same directive.
        The value for flashcachelimit cannot be smaller than flashcachemin, if it is specified.


        :param flash_cache_limit: The flash_cache_limit of this DatabasePlanDirective.
        :type: str
        """
        self._flash_cache_limit = flash_cache_limit

    @property
    def flash_cache_min(self):
        """
        Gets the flash_cache_min of this DatabasePlanDirective.
        Specifies a minimum guaranteed space allocation in Exadata Smart Flash Cache.
        You specify the value for flashcachemin in bytes. You can also use the suffixes
        M (megabytes), G (gigabytes), or T (terabytes) to specify larger values. For example, 300M, 150G, or 1T.
        The value for flashcachemin must be at least 4 MB.
        In any plan, the sum of all flashcachemin values cannot exceed the size of Exadata Smart Flash Cache.
        If flashcachelimit is specified, then the value for flashcachemin cannot exceed flashcachelimit.
        If flashcachesize is specified, then the value for flashcachemin cannot exceed flashcachesize.


        :return: The flash_cache_min of this DatabasePlanDirective.
        :rtype: str
        """
        return self._flash_cache_min

    @flash_cache_min.setter
    def flash_cache_min(self, flash_cache_min):
        """
        Sets the flash_cache_min of this DatabasePlanDirective.
        Specifies a minimum guaranteed space allocation in Exadata Smart Flash Cache.
        You specify the value for flashcachemin in bytes. You can also use the suffixes
        M (megabytes), G (gigabytes), or T (terabytes) to specify larger values. For example, 300M, 150G, or 1T.
        The value for flashcachemin must be at least 4 MB.
        In any plan, the sum of all flashcachemin values cannot exceed the size of Exadata Smart Flash Cache.
        If flashcachelimit is specified, then the value for flashcachemin cannot exceed flashcachelimit.
        If flashcachesize is specified, then the value for flashcachemin cannot exceed flashcachesize.


        :param flash_cache_min: The flash_cache_min of this DatabasePlanDirective.
        :type: str
        """
        self._flash_cache_min = flash_cache_min

    @property
    def flash_cache_size(self):
        """
        Gets the flash_cache_size of this DatabasePlanDirective.
        Defines a hard limit for space usage in Exadata Smart Flash Cache.
        The limit cannot be exceeded, even if the cache is not full.
        In an IORM plan, if the size of Exadata Smart Flash Cache can accommodate all of the flashcachemin
        and flashcachesize allocations, then each flashcachesize definition represents a guaranteed space allocation.
        However, starting with Oracle Exadata System Software release 19.2.0 you can use the flashcachesize
        attribute to over-provision space in Exadata Smart Flash Cache. Consequently,
        if the size of Exadata Smart Flash Cache cannot accommodate all of the flashcachemin and flashcachesize
        allocations, then only flashcachemin is guaranteed.


        :return: The flash_cache_size of this DatabasePlanDirective.
        :rtype: str
        """
        return self._flash_cache_size

    @flash_cache_size.setter
    def flash_cache_size(self, flash_cache_size):
        """
        Sets the flash_cache_size of this DatabasePlanDirective.
        Defines a hard limit for space usage in Exadata Smart Flash Cache.
        The limit cannot be exceeded, even if the cache is not full.
        In an IORM plan, if the size of Exadata Smart Flash Cache can accommodate all of the flashcachemin
        and flashcachesize allocations, then each flashcachesize definition represents a guaranteed space allocation.
        However, starting with Oracle Exadata System Software release 19.2.0 you can use the flashcachesize
        attribute to over-provision space in Exadata Smart Flash Cache. Consequently,
        if the size of Exadata Smart Flash Cache cannot accommodate all of the flashcachemin and flashcachesize
        allocations, then only flashcachemin is guaranteed.


        :param flash_cache_size: The flash_cache_size of this DatabasePlanDirective.
        :type: str
        """
        self._flash_cache_size = flash_cache_size

    @property
    def pmem_cache_limit(self):
        """
        Gets the pmem_cache_limit of this DatabasePlanDirective.
        Defines a soft limit for space usage in the persistent memory (PMEM) cache.
        If the cache is not full, the limit can be exceeded.
        You specify the value for pmemcachelimit in bytes. You can also use the suffixes M (megabytes),
        G (gigabytes), or T (terabytes) to specify larger values. For example, 300M, 150G, or 1T.
        The value for pmemcachelimit must be at least 4 MB.
        The pmemcachelimit and pmemcachesize attributes cannot be specified in the same directive.
        The value for pmemcachelimit cannot be smaller than pmemcachemin, if it is specified.


        :return: The pmem_cache_limit of this DatabasePlanDirective.
        :rtype: str
        """
        return self._pmem_cache_limit

    @pmem_cache_limit.setter
    def pmem_cache_limit(self, pmem_cache_limit):
        """
        Sets the pmem_cache_limit of this DatabasePlanDirective.
        Defines a soft limit for space usage in the persistent memory (PMEM) cache.
        If the cache is not full, the limit can be exceeded.
        You specify the value for pmemcachelimit in bytes. You can also use the suffixes M (megabytes),
        G (gigabytes), or T (terabytes) to specify larger values. For example, 300M, 150G, or 1T.
        The value for pmemcachelimit must be at least 4 MB.
        The pmemcachelimit and pmemcachesize attributes cannot be specified in the same directive.
        The value for pmemcachelimit cannot be smaller than pmemcachemin, if it is specified.


        :param pmem_cache_limit: The pmem_cache_limit of this DatabasePlanDirective.
        :type: str
        """
        self._pmem_cache_limit = pmem_cache_limit

    @property
    def pmem_cache_min(self):
        """
        Gets the pmem_cache_min of this DatabasePlanDirective.
        Specifies a minimum guaranteed space allocation in the persistent memory (PMEM) cache.


        :return: The pmem_cache_min of this DatabasePlanDirective.
        :rtype: str
        """
        return self._pmem_cache_min

    @pmem_cache_min.setter
    def pmem_cache_min(self, pmem_cache_min):
        """
        Sets the pmem_cache_min of this DatabasePlanDirective.
        Specifies a minimum guaranteed space allocation in the persistent memory (PMEM) cache.


        :param pmem_cache_min: The pmem_cache_min of this DatabasePlanDirective.
        :type: str
        """
        self._pmem_cache_min = pmem_cache_min

    @property
    def pmem_cache_size(self):
        """
        Gets the pmem_cache_size of this DatabasePlanDirective.
        Defines a hard limit for space usage in the persistent memory (PMEM) cache.
        The limit cannot be exceeded, even if the cache is not full.
        In an IORM plan, if the size of the PMEM cache can accommodate all of the pmemcachemin and
        pmemcachesize allocations, then each pmemcachesize definition represents a guaranteed space allocation.
        However, you can use the pmemcachesize attribute to over-provision space in the PMEM cache.
        Consequently, if the PMEM cache size cannot accommodate all of the pmemcachemin and pmemcachesize
        allocations, then only pmemcachemin is guaranteed.


        :return: The pmem_cache_size of this DatabasePlanDirective.
        :rtype: str
        """
        return self._pmem_cache_size

    @pmem_cache_size.setter
    def pmem_cache_size(self, pmem_cache_size):
        """
        Sets the pmem_cache_size of this DatabasePlanDirective.
        Defines a hard limit for space usage in the persistent memory (PMEM) cache.
        The limit cannot be exceeded, even if the cache is not full.
        In an IORM plan, if the size of the PMEM cache can accommodate all of the pmemcachemin and
        pmemcachesize allocations, then each pmemcachesize definition represents a guaranteed space allocation.
        However, you can use the pmemcachesize attribute to over-provision space in the PMEM cache.
        Consequently, if the PMEM cache size cannot accommodate all of the pmemcachemin and pmemcachesize
        allocations, then only pmemcachemin is guaranteed.


        :param pmem_cache_size: The pmem_cache_size of this DatabasePlanDirective.
        :type: str
        """
        self._pmem_cache_size = pmem_cache_size

    @property
    def asm_cluster(self):
        """
        Gets the asm_cluster of this DatabasePlanDirective.
        Starting with Oracle Exadata System Software release 19.1.0, you can use the asmcluster attribute to
        distinguish between databases with the same name running in different Oracle ASM clusters.


        :return: The asm_cluster of this DatabasePlanDirective.
        :rtype: str
        """
        return self._asm_cluster

    @asm_cluster.setter
    def asm_cluster(self, asm_cluster):
        """
        Sets the asm_cluster of this DatabasePlanDirective.
        Starting with Oracle Exadata System Software release 19.1.0, you can use the asmcluster attribute to
        distinguish between databases with the same name running in different Oracle ASM clusters.


        :param asm_cluster: The asm_cluster of this DatabasePlanDirective.
        :type: str
        """
        self._asm_cluster = asm_cluster

    @property
    def type(self):
        """
        Gets the type of this DatabasePlanDirective.
        Enables you to create a profile, or template, to ease management and configuration of resource plans
        in environments with many databases.
        type=database: Specifies a directive that applies to a specific database.
        If type in not specified, then the directive defaults to the database type.
        type=profile: Specifies a directive that applies to a profile rather than a specific database.
          To associate a database with an IORM profile, you must set the database initialization
          parameter db_performance_profile to the value of the profile name. Databases that map to a profile i
          nherit the settings specified in the profile.

        Allowed values for this property are: "DATABASE", "PROFILE", "OTHER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this DatabasePlanDirective.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DatabasePlanDirective.
        Enables you to create a profile, or template, to ease management and configuration of resource plans
        in environments with many databases.
        type=database: Specifies a directive that applies to a specific database.
        If type in not specified, then the directive defaults to the database type.
        type=profile: Specifies a directive that applies to a profile rather than a specific database.
          To associate a database with an IORM profile, you must set the database initialization
          parameter db_performance_profile to the value of the profile name. Databases that map to a profile i
          nherit the settings specified in the profile.


        :param type: The type of this DatabasePlanDirective.
        :type: str
        """
        allowed_values = ["DATABASE", "PROFILE", "OTHER"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def role(self):
        """
        Gets the role of this DatabasePlanDirective.
        Enables you specify different plan directives based on the Oracle Data Guard database role.

        Allowed values for this property are: "PRIMARY", "STANDBY", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The role of this DatabasePlanDirective.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this DatabasePlanDirective.
        Enables you specify different plan directives based on the Oracle Data Guard database role.


        :param role: The role of this DatabasePlanDirective.
        :type: str
        """
        allowed_values = ["PRIMARY", "STANDBY", "NONE"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            role = 'UNKNOWN_ENUM_VALUE'
        self._role = role

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
