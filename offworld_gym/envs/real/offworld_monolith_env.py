#!/usr/bin/env python
# Copyright offworld.ai 2018
from offworld_gym import version

__author__      = "Ashish Kumar"
__copyright__   = "Copyright offworld.ai 2019"
__license__     = "None"
__version__     = version.__version__
__maintainer__  = "Ashish Kumar"
__email__       = "ashish.kumar@offworld.ai"
__status__      = "Development"

#lib
from math import pi
import time
import numpy as np
from scipy.spatial import distance
from random import randint

#gym
import gym
from gym import utils, spaces
from offworld_gym import logger
from offworld_gym.envs.real.real_env import RealEnv
from offworld_gym.envs.common.exception.gym_exception import GymException
from offworld_gym.envs.common.channels import Channels
from offworld_gym.envs.common.actions import FourDiscreteMotionActions

class OffWorldMonolithEnv(RealEnv):
    """Real Gym environment with a rosbot and a monolith on an uneven terrain

    A RL agent learns to reach the goal(monolith) in shortest time

    Usage:
        env = gym.make('OffWorldMonolithRealEnv-v0', channel_type=Channels.DEPTHONLY)
        env = gym.make('OffWorldMonolithRealEnv-v0', channel_type=Channels.RGB_ONLY)
        env = gym.make('OffWorldMonolithRealEnv-v0', channel_type=Channels.RGBD)
    """
    _PROXIMITY_THRESHOLD = 0.20
    _EPISODE_LENGTH = 100

    def __init__(self, channel_type=Channels.DEPTH_ONLY):
        super(OffWorldMonolithEnv, self).__init__()
        
        assert isinstance(channel_type, Channels), "Channel type is not of Channels."
        logger.info("Environment has been initiated.")
        
        #environment
        self._channel_type = channel_type
        self.observation_space = spaces.Box(0, 255, shape = (1, ImageUtils.IMG_H, ImageUtils.IMG_W, channel_type.value))
        self.action_space = spaces.Discrete(4)
        self.initiate()
        self.step_count = 0
        logger.info("Environment has been started.")

    def initiate(self):
        self.secured_bridge.initiate()
        logger.info("Waiting to connect to the environment server.")
        wait_start = time.time()
        while True:
            if "STATUS_RUNNING" in self.secured_bridge.get_last_heartbeat():
                break
            else:
                continue
            if time.time() - wait_start > 60:
                raise GymException("Connect to the environment server timed out.")
        
        logger.info("The environment server is running.")

    def step(self, action):
        """Take an action in the environment

        Args:
            action: An action to be taken in the environment
        Returns:
            state: The state of the environment as captured by the robot's
                rgbd sensor
            reward: Reward from the environment
            done: A flag which is true when an episode is complete
            info: No info given for fair learning :)
        """
        
        assert action is not None, "Action cannot be None."
        assert isinstance(action, FourDiscreteMotionActions) or isinstance(action, int), "Action type is not recognized."
        self.step_count += 1

        if isinstance(action, int):
            assert action >= 0 and action < 4, "Unrecognized value for the action"
            action = FourDiscreteMotionActions(action)
        
        state, reward, done = self.secured_bridge.perform_action(action, self._channel_type)
        if self.step_count == 200:
            done = True
            self.step_count = 0
            
        return state, reward, done, {}

    def reset(self, random_step_count=10):
        """Resets the state of the environment and returns an initial observation.
        Returns:
            A numpy array with rgb/depth/rgbd encoding of the state as seen by
            the robot
        """
        self.secured_bridge.perform_reset()
        logger.info("Environment reset complete")
    
    def render(self, mode='human'):
        """
        """
        #TODO
        raise NotImplementedError