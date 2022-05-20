from . import base

list_rules = (
    base.Rule(
        name="system-admin",
        check_str=("role:admin and system_scope:all"),
        description="System scoped Administrator",
    ),
    base.Rule(
        name="system-member",
        check_str=("role:member and system_scope:all"),
        description="System scoped Member",
    ),
    base.Rule(
        name="system-reader",
        check_str=("role:reader and system_scope:all"),
        description="System scoped Reader",
    ),
    base.Rule(
        name="project-admin",
        check_str=("role:admin and project_id:%(project_id)s"),
        description="Project scoped Administrator",
    ),
    base.Rule(
        name="project-member",
        check_str=("role:member and project_id:%(project_id)s"),
        description="Project scoped Member",
    ),
    base.Rule(
        name="project-reader",
        check_str=("role:reader and project_id:%(project_id)s"),
        description="Project scoped Reader",
    ),
    base.Rule(
        name="context_is_admin",
        check_str=("rule:system-admin"),
        description='Privileged users checked via "context.is_admin"',
    ),
    base.Rule(
        name="admin_or_owner",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Administrator or Member of the project",
    ),
    base.Rule(
        name="default",
        check_str=("rule:admin_or_owner"),
        description="Default rule for most non-Admin APIs",
    ),
    base.Rule(
        name="admin_api",
        check_str=("is_admin:True"),
        description="Default rule for most Admin APIs.",
    ),
    base.APIRule(
        name="manila:availability_zone:index",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get all storage availability zones.",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/os-availability-zone"},
            {"method": "GET", "path": "/availability-zone"},
        ],
    ),
    base.APIRule(
        name="manila:scheduler_stats:pools:index",
        check_str=("(role:reader and system_scope:all)"),
        description="Get information regarding backends (and storage pools) known to the scheduler.",  # noqa
        scope_types=["system"],
        operations=[
            {"method": "GET", "path": "/scheduler-stats/pools"},
            {"method": "GET", "path": "/scheduler-stats/pools?{query}"},
        ],
    ),
    base.APIRule(
        name="manila:scheduler_stats:pools:detail",
        check_str=("(role:reader and system_scope:all)"),
        description="Get detailed information regarding backends (and storage pools) known to the scheduler.",  # noqa
        scope_types=["system"],
        operations=[
            {"method": "GET", "path": "/scheduler-stats/pools/detail?{query}"},
            {"method": "GET", "path": "/scheduler-stats/pools/detail"},
        ],
    ),
    base.APIRule(
        name="manila:share:create",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Create share.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/shares"}],
    ),
    base.APIRule(
        name="manila:share:create_public_share",
        check_str=("(role:admin and system_scope:all)"),
        description="Create shares visible across all projects in the cloud.",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/shares"}],
    ),
    base.APIRule(
        name="manila:share:get",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get share.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/shares/{share_id}"}],
    ),
    base.APIRule(
        name="manila:share:get_all",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="List shares.",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/shares"},
            {"method": "GET", "path": "/shares/detail"},
        ],
    ),
    base.APIRule(
        name="manila:share:update",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Update share.",
        scope_types=["system", "project"],
        operations=[{"method": "PUT", "path": "/shares"}],
    ),
    base.APIRule(
        name="manila:share:set_public_share",
        check_str=("(role:admin and system_scope:all)"),
        description="Update shares to be visible across all projects in the cloud.",
        scope_types=["system"],
        operations=[{"method": "PUT", "path": "/shares"}],
    ),
    base.APIRule(
        name="manila:share:delete",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Delete share.",
        scope_types=["system", "project"],
        operations=[{"method": "DELETE", "path": "/shares/{share_id}"}],
    ),
    base.APIRule(
        name="manila:share:soft_delete",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Soft Delete a share.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/shares/{share_id}/action"}],
    ),
    base.APIRule(
        name="manila:share:restore",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Restore a share.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/shares/{share_id}/action"}],
    ),
    base.APIRule(
        name="manila:share:force_delete",
        check_str=(
            "(role:admin and system_scope:all) or (role:admin and project_id:%(project_id)s)"
        ),
        description="Force Delete a share.",
        scope_types=["system", "project"],
        operations=[{"method": "DELETE", "path": "/shares/{share_id}"}],
    ),
    base.APIRule(
        name="manila:share:manage",
        check_str=("(role:admin and system_scope:all)"),
        description="Manage share.",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/shares/manage"}],
    ),
    base.APIRule(
        name="manila:share:unmanage",
        check_str=("(role:admin and system_scope:all)"),
        description="Unmanage share.",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/shares/unmanage"}],
    ),
    base.APIRule(
        name="manila:share:list_by_host",
        check_str=("(role:reader and system_scope:all)"),
        description="List share by host.",
        scope_types=["system"],
        operations=[
            {"method": "GET", "path": "/shares"},
            {"method": "GET", "path": "/shares/detail"},
        ],
    ),
    base.APIRule(
        name="manila:share:list_by_share_server_id",
        check_str=("(role:reader and system_scope:all)"),
        description="List share by server id.",
        scope_types=["system"],
        operations=[
            {"method": "GET", "path": "/shares"},
            {"method": "GET", "path": "/shares/detail"},
        ],
    ),
    base.APIRule(
        name="manila:share:access_get",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get share access rule, it under deny access operation.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/shares/{share_id}/action"}],
    ),
    base.APIRule(
        name="manila:share:access_get_all",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="List share access rules.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/shares/{share_id}/action"}],
    ),
    base.APIRule(
        name="manila:share:extend",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Extend share.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/shares/{share_id}/action"}],
    ),
    base.APIRule(
        name="manila:share:force_extend",
        check_str=(
            "(role:admin and system_scope:all) or (role:admin and project_id:%(project_id)s)"
        ),
        description="Force extend share.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/shares/{share_id}/action"}],
    ),
    base.APIRule(
        name="manila:share:shrink",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Shrink share.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/shares/{share_id}/action"}],
    ),
    base.APIRule(
        name="manila:share:migration_start",
        check_str=("(role:admin and system_scope:all)"),
        description="Migrate a share to the specified host.",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/shares/{share_id}/action"}],
    ),
    base.APIRule(
        name="manila:share:migration_complete",
        check_str=("(role:admin and system_scope:all)"),
        description="Invokes 2nd phase of share migration.",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/shares/{share_id}/action"}],
    ),
    base.APIRule(
        name="manila:share:migration_cancel",
        check_str=("(role:admin and system_scope:all)"),
        description="Attempts to cancel share migration.",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/shares/{share_id}/action"}],
    ),
    base.APIRule(
        name="manila:share:migration_get_progress",
        check_str=("(role:reader and system_scope:all)"),
        description="Retrieve share migration progress for a given share.",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/shares/{share_id}/action"}],
    ),
    base.APIRule(
        name="manila:share:reset_task_state",
        check_str=(
            "(role:admin and system_scope:all) or (role:admin and project_id:%(project_id)s)"
        ),
        description="Reset task state.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/shares/{share_id}/action"}],
    ),
    base.APIRule(
        name="manila:share:reset_status",
        check_str=(
            "(role:admin and system_scope:all) or (role:admin and project_id:%(project_id)s)"
        ),
        description="Reset status.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/shares/{share_id}/action"}],
    ),
    base.APIRule(
        name="manila:share:revert_to_snapshot",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Revert a share to a snapshot.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/shares/{share_id}/action"}],
    ),
    base.APIRule(
        name="manila:share:allow_access",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Add share access rule.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/shares/{share_id}/action"}],
    ),
    base.APIRule(
        name="manila:share:deny_access",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Remove share access rule.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/shares/{share_id}/action"}],
    ),
    base.APIRule(
        name="manila:share:update_share_metadata",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Update share metadata.",
        scope_types=["system", "project"],
        operations=[
            {"method": "PUT", "path": "/shares/{share_id}/metadata"},
            {"method": "POST", "path": "/shares/{share_id}/metadata/{key}"},
            {"method": "POST", "path": "/shares/{share_id}/metadata"},
        ],
    ),
    base.APIRule(
        name="manila:share:delete_share_metadata",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Delete share metadata.",
        scope_types=["system", "project"],
        operations=[{"method": "DELETE", "path": "/shares/{share_id}/metadata/{key}"}],
    ),
    base.APIRule(
        name="manila:share:get_share_metadata",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get share metadata.",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/shares/{share_id}/metadata"},
            {"method": "GET", "path": "/shares/{share_id}/metadata/{key}"},
        ],
    ),
    base.APIRule(
        name="manila:share:create_snapshot",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Create share snapshot.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/snapshots"}],
    ),
    base.APIRule(
        name="manila:share:delete_snapshot",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Delete share snapshot.",
        scope_types=["system", "project"],
        operations=[{"method": "DELETE", "path": "/snapshots/{snapshot_id}"}],
    ),
    base.APIRule(
        name="manila:share:snapshot_update",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Update share snapshot.",
        scope_types=["system", "project"],
        operations=[{"method": "PUT", "path": "/snapshots/{snapshot_id}/action"}],
    ),
    base.APIRule(
        name="manila:share:update_admin_only_metadata",
        check_str=(
            "(role:admin and system_scope:all) or (role:admin and project_id:%(project_id)s)"
        ),
        description='Update metadata items that are considered "admin only" by the service.',
        scope_types=["system", "project"],
        operations=[{"method": "PUT", "path": "/shares/{share_id}/metadata"}],
    ),
    base.APIRule(
        name="manila:share_instance_export_location:index",
        check_str=("(role:reader and system_scope:all)"),
        description="Return data about the requested export location.",
        scope_types=["system"],
        operations=[
            {"method": "POST", "path": "/share_instances/{share_instance_id}/export_locations"},
        ],
    ),
    base.APIRule(
        name="manila:share_instance_export_location:show",
        check_str=("(role:reader and system_scope:all)"),
        description="Return data about the requested export location.",
        scope_types=["system"],
        operations=[
            {
                "method": "GET",
                "path": "/share_instances/{share_instance_id}/export_locations/{export_location_id}",  # noqa
            },
        ],
    ),
    base.APIRule(
        name="manila:share_type:create",
        check_str=("(role:admin and system_scope:all)"),
        description="Create share type.",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/types"}],
    ),
    base.APIRule(
        name="manila:share_type:update",
        check_str=("(role:admin and system_scope:all)"),
        description="Update share type.",
        scope_types=["system"],
        operations=[{"method": "PUT", "path": "/types/{share_type_id}"}],
    ),
    base.APIRule(
        name="manila:share_type:show",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get share type.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/types/{share_type_id}"}],
    ),
    base.APIRule(
        name="manila:share_type:index",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="List share types.",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/types"},
            {"method": "GET", "path": "/types?is_public=all"},
        ],
    ),
    base.APIRule(
        name="manila:share_type:default",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get default share type.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/types/default"}],
    ),
    base.APIRule(
        name="manila:share_type:delete",
        check_str=("(role:admin and system_scope:all)"),
        description="Delete share type.",
        scope_types=["system"],
        operations=[{"method": "DELETE", "path": "/types/{share_type_id}"}],
    ),
    base.APIRule(
        name="manila:share_type:list_project_access",
        check_str=("(role:reader and system_scope:all)"),
        description="List share type project access.",
        scope_types=["system"],
        operations=[{"method": "GET", "path": "/types/{share_type_id}"}],
    ),
    base.APIRule(
        name="manila:share_type:add_project_access",
        check_str=("(role:admin and system_scope:all)"),
        description="Add share type to project.",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/types/{share_type_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_type:remove_project_access",
        check_str=("(role:admin and system_scope:all)"),
        description="Remove share type from project.",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/types/{share_type_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_types_extra_spec:create",
        check_str=("(role:admin and system_scope:all)"),
        description="Create share type extra spec.",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/types/{share_type_id}/extra_specs"}],
    ),
    base.APIRule(
        name="manila:share_types_extra_spec:show",
        check_str=("(role:reader and system_scope:all)"),
        description="Get share type extra specs of a given share type.",
        scope_types=["system"],
        operations=[{"method": "GET", "path": "/types/{share_type_id}/extra_specs"}],
    ),
    base.APIRule(
        name="manila:share_types_extra_spec:index",
        check_str=("(role:reader and system_scope:all)"),
        description="Get details of a share type extra spec.",
        scope_types=["system"],
        operations=[
            {"method": "GET", "path": "/types/{share_type_id}/extra_specs/{extra_spec_id}"},
        ],
    ),
    base.APIRule(
        name="manila:share_types_extra_spec:update",
        check_str=("(role:admin and system_scope:all)"),
        description="Update share type extra spec.",
        scope_types=["system"],
        operations=[{"method": "PUT", "path": "/types/{share_type_id}/extra_specs"}],
    ),
    base.APIRule(
        name="manila:share_types_extra_spec:delete",
        check_str=("(role:admin and system_scope:all)"),
        description="Delete share type extra spec.",
        scope_types=["system"],
        operations=[{"method": "DELETE", "path": "/types/{share_type_id}/extra_specs/{key}"}],
    ),
    base.APIRule(
        name="manila:share_snapshot:get_snapshot",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get share snapshot.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/snapshots/{snapshot_id}"}],
    ),
    base.APIRule(
        name="manila:share_snapshot:get_all_snapshots",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get all share snapshots.",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/snapshots"},
            {"method": "GET", "path": "/snapshots/detail"},
            {"method": "GET", "path": "/snapshots?{query}"},
            {"method": "GET", "path": "/snapshots/detail?{query}"},
        ],
    ),
    base.APIRule(
        name="manila:share_snapshot:force_delete",
        check_str=(
            "(role:admin and system_scope:all) or (role:admin and project_id:%(project_id)s)"
        ),
        description="Force Delete a share snapshot.",
        scope_types=["system", "project"],
        operations=[{"method": "DELETE", "path": "/snapshots/{snapshot_id}"}],
    ),
    base.APIRule(
        name="manila:share_snapshot:manage_snapshot",
        check_str=("(role:admin and system_scope:all)"),
        description="Manage share snapshot.",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/snapshots/manage"}],
    ),
    base.APIRule(
        name="manila:share_snapshot:unmanage_snapshot",
        check_str=("(role:admin and system_scope:all)"),
        description="Unmanage share snapshot.",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/snapshots/{snapshot_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_snapshot:reset_status",
        check_str=(
            "(role:admin and system_scope:all) or (role:admin and project_id:%(project_id)s)"
        ),
        description="Reset status.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/snapshots/{snapshot_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_snapshot:access_list",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="List access rules of a share snapshot.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/snapshots/{snapshot_id}/access-list"}],
    ),
    base.APIRule(
        name="manila:share_snapshot:allow_access",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Allow access to a share snapshot.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/snapshots/{snapshot_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_snapshot:deny_access",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Deny access to a share snapshot.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/snapshots/{snapshot_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_snapshot_export_location:index",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="List export locations of a share snapshot.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/snapshots/{snapshot_id}/export-locations/"}],
    ),
    base.APIRule(
        name="manila:share_snapshot_export_location:show",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get details of a specified export location of a share snapshot.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "GET",
                "path": "/snapshots/{snapshot_id}/export-locations/{export_location_id}",
            },
        ],
    ),
    base.APIRule(
        name="manila:share_snapshot_instance:show",
        check_str=("(role:reader and system_scope:all)"),
        description="Get share snapshot instance.",
        scope_types=["system"],
        operations=[{"method": "GET", "path": "/snapshot-instances/{snapshot_instance_id}"}],
    ),
    base.APIRule(
        name="manila:share_snapshot_instance:index",
        check_str=("(role:reader and system_scope:all)"),
        description="Get all share snapshot instances.",
        scope_types=["system"],
        operations=[
            {"method": "GET", "path": "/snapshot-instances"},
            {"method": "GET", "path": "/snapshot-instances?{query}"},
        ],
    ),
    base.APIRule(
        name="manila:share_snapshot_instance:detail",
        check_str=("(role:reader and system_scope:all)"),
        description="Get details of share snapshot instances.",
        scope_types=["system"],
        operations=[
            {"method": "GET", "path": "/snapshot-instances/detail"},
            {"method": "GET", "path": "/snapshot-instances/detail?{query}"},
        ],
    ),
    base.APIRule(
        name="manila:share_snapshot_instance:reset_status",
        check_str=("(role:admin and system_scope:all)"),
        description="Reset share snapshot instance's status.",
        scope_types=["system"],
        operations=[
            {"method": "POST", "path": "/snapshot-instances/{snapshot_instance_id}/action"},
        ],
    ),
    base.APIRule(
        name="manila:share_snapshot_instance_export_location:index",
        check_str=("(role:reader and system_scope:all)"),
        description="List export locations of a share snapshot instance.",
        scope_types=["system"],
        operations=[
            {
                "method": "GET",
                "path": "/snapshot-instances/{snapshot_instance_id}/export-locations",
            },
        ],
    ),
    base.APIRule(
        name="manila:share_snapshot_instance_export_location:show",
        check_str=("(role:reader and system_scope:all)"),
        description="Show details of a specified export location of a share snapshot instance.",
        scope_types=["system"],
        operations=[
            {
                "method": "GET",
                "path": "/snapshot-instances/{snapshot_instance_id}/export-locations/{export_location_id}",  # noqa
            },
        ],
    ),
    base.APIRule(
        name="manila:share_server:index",
        check_str=("(role:reader and system_scope:all)"),
        description="Get share servers.",
        scope_types=["system"],
        operations=[
            {"method": "GET", "path": "/share-servers"},
            {"method": "GET", "path": "/share-servers?{query}"},
        ],
    ),
    base.APIRule(
        name="manila:share_server:show",
        check_str=("(role:reader and system_scope:all)"),
        description="Show share server.",
        scope_types=["system"],
        operations=[{"method": "GET", "path": "/share-servers/{server_id}"}],
    ),
    base.APIRule(
        name="manila:share_server:details",
        check_str=("(role:reader and system_scope:all)"),
        description="Get share server details.",
        scope_types=["system"],
        operations=[{"method": "GET", "path": "/share-servers/{server_id}/details"}],
    ),
    base.APIRule(
        name="manila:share_server:delete",
        check_str=("(role:admin and system_scope:all)"),
        description="Delete share server.",
        scope_types=["system"],
        operations=[{"method": "DELETE", "path": "/share-servers/{server_id}"}],
    ),
    base.APIRule(
        name="manila:share_server:manage_share_server",
        check_str=("(role:admin and system_scope:all)"),
        description="Manage share server.",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/share-servers/manage"}],
    ),
    base.APIRule(
        name="manila:share_server:unmanage_share_server",
        check_str=("(role:admin and system_scope:all)"),
        description="Unmanage share server.",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/share-servers/{share_server_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_server:reset_status",
        check_str=("(role:admin and system_scope:all)"),
        description="Reset the status of a share server.",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/share-servers/{share_server_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_server:share_server_migration_start",
        check_str=("(role:admin and system_scope:all)"),
        description="Migrates a share server to the specified host.",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/share-servers/{share_server_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_server:share_server_migration_check",
        check_str=("(role:reader and system_scope:all)"),
        description="Check if can migrates a share server to the specified host.",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/share-servers/{share_server_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_server:share_server_migration_complete",
        check_str=("(role:admin and system_scope:all)"),
        description="Invokes the 2nd phase of share server migration.",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/share-servers/{share_server_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_server:share_server_migration_cancel",
        check_str=("(role:admin and system_scope:all)"),
        description="Attempts to cancel share server migration.",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/share-servers/{share_server_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_server:share_server_migration_get_progress",
        check_str=("(role:reader and system_scope:all)"),
        description="Retrieves the share server migration progress for a given share server.",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/share-servers/{share_server_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_server:share_server_reset_task_state",
        check_str=("(role:admin and system_scope:all)"),
        description="Resets task state.",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/share-servers/{share_server_id}/action"}],
    ),
    base.APIRule(
        name="manila:service:index",
        check_str=("(role:reader and system_scope:all)"),
        description="Return a list of all running services.",
        scope_types=["system"],
        operations=[
            {"method": "GET", "path": "/os-services"},
            {"method": "GET", "path": "/os-services?{query}"},
            {"method": "GET", "path": "/services"},
            {"method": "GET", "path": "/services?{query}"},
        ],
    ),
    base.APIRule(
        name="manila:service:update",
        check_str=("(role:admin and system_scope:all)"),
        description="Enable/Disable scheduling for a service.",
        scope_types=["system"],
        operations=[
            {"method": "PUT", "path": "/os-services/disable"},
            {"method": "PUT", "path": "/os-services/enable"},
            {"method": "PUT", "path": "/services/disable"},
            {"method": "PUT", "path": "/services/enable"},
        ],
    ),
    base.APIRule(
        name="manila:quota_set:update",
        check_str=("(role:admin and system_scope:all)"),
        description="Update the quotas for a project/user and/or share type.",
        scope_types=["system"],
        operations=[
            {"method": "PUT", "path": "/quota-sets/{tenant_id}"},
            {"method": "PUT", "path": "/quota-sets/{tenant_id}?user_id={user_id}"},
            {"method": "PUT", "path": "/quota-sets/{tenant_id}?share_type={share_type_id}"},
            {"method": "PUT", "path": "/os-quota-sets/{tenant_id}"},
            {"method": "PUT", "path": "/os-quota-sets/{tenant_id}?user_id={user_id}"},
        ],
    ),
    base.APIRule(
        name="manila:quota_set:show",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="List the quotas for a tenant/user.",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/quota-sets/{tenant_id}/defaults"},
            {"method": "GET", "path": "/os-quota-sets/{tenant_id}/defaults"},
        ],
    ),
    base.APIRule(
        name="manila:quota_set:delete",
        check_str=("(role:admin and system_scope:all)"),
        description="Delete quota for a tenant/user or tenant/share-type. The quota will revert back to default (Admin only).",  # noqa
        scope_types=["system"],
        operations=[
            {"method": "DELETE", "path": "/quota-sets/{tenant_id}"},
            {"method": "DELETE", "path": "/quota-sets/{tenant_id}?user_id={user_id}"},
            {"method": "DELETE", "path": "/quota-sets/{tenant_id}?share_type={share_type_id}"},
            {"method": "DELETE", "path": "/os-quota-sets/{tenant_id}"},
            {"method": "DELETE", "path": "/os-quota-sets/{tenant_id}?user_id={user_id}"},
        ],
    ),
    base.APIRule(
        name="manila:quota_class_set:update",
        check_str=("(role:admin and system_scope:all)"),
        description="Update quota class.",
        scope_types=["system"],
        operations=[
            {"method": "PUT", "path": "/quota-class-sets/{class_name}"},
            {"method": "PUT", "path": "/os-quota-class-sets/{class_name}"},
        ],
    ),
    base.APIRule(
        name="manila:quota_class_set:show",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get quota class.",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/quota-class-sets/{class_name}"},
            {"method": "GET", "path": "/os-quota-class-sets/{class_name}"},
        ],
    ),
    base.APIRule(
        name="manila:share_group_types_spec:create",
        check_str=("(role:admin and system_scope:all)"),
        description="Create share group type specs.",
        scope_types=["system"],
        operations=[
            {"method": "POST", "path": "/share-group-types/{share_group_type_id}/group-specs"},
        ],
    ),
    base.APIRule(
        name="manila:share_group_types_spec:index",
        check_str=("(role:reader and system_scope:all)"),
        description="Get share group type specs.",
        scope_types=["system"],
        operations=[
            {"method": "GET", "path": "/share-group-types/{share_group_type_id}/group-specs"},
        ],
    ),
    base.APIRule(
        name="manila:share_group_types_spec:show",
        check_str=("(role:reader and system_scope:all)"),
        description="Get details of a share group type spec.",
        scope_types=["system"],
        operations=[
            {
                "method": "GET",
                "path": "/share-group-types/{share_group_type_id}/group-specs/{key}",
            },
        ],
    ),
    base.APIRule(
        name="manila:share_group_types_spec:update",
        check_str=("(role:admin and system_scope:all)"),
        description="Update a share group type spec.",
        scope_types=["system"],
        operations=[
            {
                "method": "PUT",
                "path": "/share-group-types/{share_group_type_id}/group-specs/{key}",
            },
        ],
    ),
    base.APIRule(
        name="manila:share_group_types_spec:delete",
        check_str=("(role:admin and system_scope:all)"),
        description="Delete a share group type spec.",
        scope_types=["system"],
        operations=[
            {
                "method": "DELETE",
                "path": "/share-group-types/{share_group_type_id}/group-specs/{key}",
            },
        ],
    ),
    base.APIRule(
        name="manila:share_group_type:create",
        check_str=("(role:admin and system_scope:all)"),
        description="Create a new share group type.",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/share-group-types"}],
    ),
    base.APIRule(
        name="manila:share_group_type:index",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get the list of share group types.",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/share-group-types"},
            {"method": "GET", "path": "/share-group-types?is_public=all"},
        ],
    ),
    base.APIRule(
        name="manila:share_group_type:show",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get details regarding the specified share group type.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/share-group-types/{share_group_type_id}"}],
    ),
    base.APIRule(
        name="manila:share_group_type:default",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get the default share group type.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/share-group-types/default"}],
    ),
    base.APIRule(
        name="manila:share_group_type:delete",
        check_str=("(role:admin and system_scope:all)"),
        description="Delete an existing group type.",
        scope_types=["system"],
        operations=[{"method": "DELETE", "path": "/share-group-types/{share_group_type_id}"}],
    ),
    base.APIRule(
        name="manila:share_group_type:list_project_access",
        check_str=("(role:reader and system_scope:all)"),
        description="Get project access by share group type.",
        scope_types=["system"],
        operations=[{"method": "GET", "path": "/share-group-types/{share_group_type_id}/access"}],
    ),
    base.APIRule(
        name="manila:share_group_type:add_project_access",
        check_str=("(role:admin and system_scope:all)"),
        description="Allow project to use the share group type.",
        scope_types=["system"],
        operations=[
            {"method": "POST", "path": "/share-group-types/{share_group_type_id}/action"},
        ],
    ),
    base.APIRule(
        name="manila:share_group_type:remove_project_access",
        check_str=("(role:admin and system_scope:all)"),
        description="Deny project access to use the share group type.",
        scope_types=["system"],
        operations=[
            {"method": "POST", "path": "/share-group-types/{share_group_type_id}/action"},
        ],
    ),
    base.APIRule(
        name="manila:share_group_snapshot:create",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Create a new share group snapshot.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/share-group-snapshots"}],
    ),
    base.APIRule(
        name="manila:share_group_snapshot:get",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get details of a share group snapshot.",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/share-group-snapshots/{share_group_snapshot_id}"},
        ],
    ),
    base.APIRule(
        name="manila:share_group_snapshot:get_all",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get all share group snapshots.",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/share-group-snapshots"},
            {"method": "GET", "path": "/share-group-snapshots/detail"},
            {"method": "GET", "path": "/share-group-snapshots/{query}"},
            {"method": "GET", "path": "/share-group-snapshots/detail?{query}"},
        ],
    ),
    base.APIRule(
        name="manila:share_group_snapshot:update",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Update a share group snapshot.",
        scope_types=["system", "project"],
        operations=[
            {"method": "PUT", "path": "/share-group-snapshots/{share_group_snapshot_id}"},
        ],
    ),
    base.APIRule(
        name="manila:share_group_snapshot:delete",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Delete a share group snapshot.",
        scope_types=["system", "project"],
        operations=[
            {"method": "DELETE", "path": "/share-group-snapshots/{share_group_snapshot_id}"},
        ],
    ),
    base.APIRule(
        name="manila:share_group_snapshot:force_delete",
        check_str=(
            "(role:admin and system_scope:all) or (role:admin and project_id:%(project_id)s)"
        ),
        description="Force delete a share group snapshot.",
        scope_types=["system", "project"],
        operations=[
            {"method": "POST", "path": "/share-group-snapshots/{share_group_snapshot_id}/action"},
        ],
    ),
    base.APIRule(
        name="manila:share_group_snapshot:reset_status",
        check_str=(
            "(role:admin and system_scope:all) or (role:admin and project_id:%(project_id)s)"
        ),
        description="Reset a share group snapshot's status.",
        scope_types=["system", "project"],
        operations=[
            {"method": "POST", "path": "/share-group-snapshots/{share_group_snapshot_id}/action"},
        ],
    ),
    base.APIRule(
        name="manila:share_group:create",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Create share group.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/share-groups"}],
    ),
    base.APIRule(
        name="manila:share_group:get",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get details of a share group.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/share-groups/{share_group_id}"}],
    ),
    base.APIRule(
        name="manila:share_group:get_all",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get all share groups.",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/share-groups"},
            {"method": "GET", "path": "/share-groups/detail"},
            {"method": "GET", "path": "/share-groups?{query}"},
            {"method": "GET", "path": "/share-groups/detail?{query}"},
        ],
    ),
    base.APIRule(
        name="manila:share_group:update",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Update share group.",
        scope_types=["system", "project"],
        operations=[{"method": "PUT", "path": "/share-groups/{share_group_id}"}],
    ),
    base.APIRule(
        name="manila:share_group:delete",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Delete share group.",
        scope_types=["system", "project"],
        operations=[{"method": "DELETE", "path": "/share-groups/{share_group_id}"}],
    ),
    base.APIRule(
        name="manila:share_group:force_delete",
        check_str=(
            "(role:admin and system_scope:all) or (role:admin and project_id:%(project_id)s)"
        ),
        description="Force delete a share group.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/share-groups/{share_group_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_group:reset_status",
        check_str=(
            "(role:admin and system_scope:all) or (role:admin and project_id:%(project_id)s)"
        ),
        description="Reset share group's status.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/share-groups/{share_group_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_replica:create",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Create share replica.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/share-replicas"}],
    ),
    base.APIRule(
        name="manila:share_replica:get_all",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get all share replicas.",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/share-replicas"},
            {"method": "GET", "path": "/share-replicas/detail"},
            {"method": "GET", "path": "/share-replicas/detail?share_id={share_id}"},
        ],
    ),
    base.APIRule(
        name="manila:share_replica:show",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get details of a share replica.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/share-replicas/{share_replica_id}"}],
    ),
    base.APIRule(
        name="manila:share_replica:delete",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Delete a share replica.",
        scope_types=["system", "project"],
        operations=[{"method": "DELETE", "path": "/share-replicas/{share_replica_id}"}],
    ),
    base.APIRule(
        name="manila:share_replica:force_delete",
        check_str=(
            "(role:admin and system_scope:all) or (role:admin and project_id:%(project_id)s)"
        ),
        description="Force delete a share replica.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/share-replicas/{share_replica_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_replica:promote",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Promote a non-active share replica to active.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/share-replicas/{share_replica_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_replica:resync",
        check_str=(
            "(role:admin and system_scope:all) or (role:admin and project_id:%(project_id)s)"
        ),
        description="Resync a share replica that is out of sync.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/share-replicas/{share_replica_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_replica:reset_replica_state",
        check_str=(
            "(role:admin and system_scope:all) or (role:admin and project_id:%(project_id)s)"
        ),
        description="Reset share replica's replica_state attribute.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/share-replicas/{share_replica_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_replica:reset_status",
        check_str=(
            "(role:admin and system_scope:all) or (role:admin and project_id:%(project_id)s)"
        ),
        description="Reset share replica's status.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/share-replicas/{share_replica_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_replica_export_location:index",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get all export locations of a given share replica.",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/share-replicas/{share_replica_id}/export-locations"},
        ],
    ),
    base.APIRule(
        name="manila:share_replica_export_location:show",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get details about the requested share replica export location.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "GET",
                "path": "/share-replicas/{share_replica_id}/export-locations/{export_location_id}",
            },
        ],
    ),
    base.APIRule(
        name="manila:share_network:create",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Create share network.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/share-networks"}],
    ),
    base.APIRule(
        name="manila:share_network:show",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get details of a share network.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/share-networks/{share_network_id}"}],
    ),
    base.APIRule(
        name="manila:share_network:index",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get all share networks.",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/share-networks"},
            {"method": "GET", "path": "/share-networks?{query}"},
        ],
    ),
    base.APIRule(
        name="manila:share_network:detail",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get details of share networks .",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/share-networks/detail?{query}"},
            {"method": "GET", "path": "/share-networks/detail"},
        ],
    ),
    base.APIRule(
        name="manila:share_network:update",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Update a share network.",
        scope_types=["system", "project"],
        operations=[{"method": "PUT", "path": "/share-networks/{share_network_id}"}],
    ),
    base.APIRule(
        name="manila:share_network:delete",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Delete a share network.",
        scope_types=["system", "project"],
        operations=[{"method": "DELETE", "path": "/share-networks/{share_network_id}"}],
    ),
    base.APIRule(
        name="manila:share_network:add_security_service",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Add security service to share network.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/share-networks/{share_network_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_network:add_security_service_check",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Check the feasibility of add security service to a share network.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/share-networks/{share_network_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_network:remove_security_service",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Remove security service from share network.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/share-networks/{share_network_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_network:update_security_service",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Update security service from share network.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/share-networks/{share_network_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_network:update_security_service_check",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Check the feasibility of update a security service from share network.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/share-networks/{share_network_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_network:reset_status",
        check_str=(
            "(role:admin and system_scope:all) or (role:admin and project_id:%(project_id)s)"
        ),
        description="Reset share network`s status.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/share-networks/{share_network_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_network:get_all_share_networks",
        check_str=("(role:reader and system_scope:all)"),
        description="Get share networks belonging to all projects.",
        scope_types=["system"],
        operations=[
            {"method": "GET", "path": "/share-networks?all_tenants=1"},
            {"method": "GET", "path": "/share-networks/detail?all_tenants=1"},
        ],
    ),
    base.APIRule(
        name="manila:share_network:subnet_create_check",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Check the feasibility of create a new share network subnet for share network.",  # noqa
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/share-networks/{share_network_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_network_subnet:create",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Create a new share network subnet.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/share-networks/{share_network_id}/subnets"}],
    ),
    base.APIRule(
        name="manila:share_network_subnet:delete",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Delete a share network subnet.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "DELETE",
                "path": "/share-networks/{share_network_id}/subnets/{share_network_subnet_id}",
            },
        ],
    ),
    base.APIRule(
        name="manila:share_network_subnet:show",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Shows a share network subnet.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "GET",
                "path": "/share-networks/{share_network_id}/subnets/{share_network_subnet_id}",
            },
        ],
    ),
    base.APIRule(
        name="manila:share_network_subnet:index",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get all share network subnets.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/share-networks/{share_network_id}/subnets"}],
    ),
    base.APIRule(
        name="manila:security_service:create",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Create security service.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/security-services"}],
    ),
    base.APIRule(
        name="manila:security_service:show",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get details of a security service.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/security-services/{security_service_id}"}],
    ),
    base.APIRule(
        name="manila:security_service:detail",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get details of all security services.",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/security-services/detail?{query}"},
            {"method": "GET", "path": "/security-services/detail"},
        ],
    ),
    base.APIRule(
        name="manila:security_service:index",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get all security services.",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/security-services"},
            {"method": "GET", "path": "/security-services?{query}"},
        ],
    ),
    base.APIRule(
        name="manila:security_service:update",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Update a security service.",
        scope_types=["system", "project"],
        operations=[{"method": "PUT", "path": "/security-services/{security_service_id}"}],
    ),
    base.APIRule(
        name="manila:security_service:delete",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Delete a security service.",
        scope_types=["system", "project"],
        operations=[{"method": "DELETE", "path": "/security-services/{security_service_id}"}],
    ),
    base.APIRule(
        name="manila:security_service:get_all_security_services",
        check_str=("(role:reader and system_scope:all)"),
        description="Get security services of all projects.",
        scope_types=["system"],
        operations=[
            {"method": "GET", "path": "/security-services?all_tenants=1"},
            {"method": "GET", "path": "/security-services/detail?all_tenants=1"},
        ],
    ),
    base.APIRule(
        name="manila:share_export_location:index",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get all export locations of a given share.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/shares/{share_id}/export_locations"}],
    ),
    base.APIRule(
        name="manila:share_export_location:show",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get details about the requested export location.",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/shares/{share_id}/export_locations/{export_location_id}"},
        ],
    ),
    base.APIRule(
        name="manila:share_instance:index",
        check_str=("(role:reader and system_scope:all)"),
        description="Get all share instances.",
        scope_types=["system"],
        operations=[
            {"method": "GET", "path": "/share_instances"},
            {"method": "GET", "path": "/share_instances?{query}"},
        ],
    ),
    base.APIRule(
        name="manila:share_instance:show",
        check_str=("(role:reader and system_scope:all)"),
        description="Get details of a share instance.",
        scope_types=["system"],
        operations=[{"method": "GET", "path": "/share_instances/{share_instance_id}"}],
    ),
    base.APIRule(
        name="manila:share_instance:force_delete",
        check_str=("(role:admin and system_scope:all)"),
        description="Force delete a share instance.",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/share_instances/{share_instance_id}/action"}],
    ),
    base.APIRule(
        name="manila:share_instance:reset_status",
        check_str=("(role:admin and system_scope:all)"),
        description="Reset share instance's status.",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/share_instances/{share_instance_id}/action"}],
    ),
    base.APIRule(
        name="manila:message:get",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get details of a given message.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/messages/{message_id}"}],
    ),
    base.APIRule(
        name="manila:message:get_all",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get all messages.",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/messages"},
            {"method": "GET", "path": "/messages?{query}"},
        ],
    ),
    base.APIRule(
        name="manila:message:delete",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Delete a message.",
        scope_types=["system", "project"],
        operations=[{"method": "DELETE", "path": "/messages/{message_id}"}],
    ),
    base.APIRule(
        name="manila:share_access_rule:get",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get details of a share access rule.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/share-access-rules/{share_access_id}"}],
    ),
    base.APIRule(
        name="manila:share_access_rule:index",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="List access rules of a given share.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "GET",
                "path": "/share-access-rules?share_id={share_id}&key1=value1&key2=value2",
            },
        ],
    ),
    base.APIRule(
        name="manila:share_access_metadata:update",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Set metadata for a share access rule.",
        scope_types=["system", "project"],
        operations=[{"method": "PUT", "path": "/share-access-rules/{share_access_id}/metadata"}],
    ),
    base.APIRule(
        name="manila:share_access_metadata:delete",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Delete metadata for a share access rule.",
        scope_types=["system", "project"],
        operations=[
            {"method": "DELETE", "path": "/share-access-rules/{share_access_id}/metadata/{key}"},
        ],
    ),
)

__all__ = ("list_rules",)