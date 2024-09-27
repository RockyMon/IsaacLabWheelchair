# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Configuration for the wheelchair

The following configurations are available:


"""

import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.actuators import ImplicitActuatorCfg
from omni.isaac.lab.assets.articulation import ArticulationCfg

##
# Configuration
##

WHEELCHAIR_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"/home/robot/Downloads/wheelchair/wheelchair.usd",
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(enabled_self_collisions=True),
        activate_contact_sensors=True,rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        joint_pos={
            # base
            "joint_BackWheel_L": 0.0,
            "joint_BackWheel_R": 0.0,
            "joint_frontSupport_L": 0.0,
            "joint_frontSupport_R": 0.0
            
            
        },
        joint_vel={".*": 0.0},
    ),
    actuators={
        "base": ImplicitActuatorCfg(
            joint_names_expr=["joint_.*"],
            velocity_limit=100.0,
            effort_limit=1000.0,
            stiffness=0.0,
            damping=1e5,
        )
    },
)


