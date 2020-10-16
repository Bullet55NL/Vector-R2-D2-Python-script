#!/usr/bin/env python3

# Copyright (c) 2018 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# R2D2 script by @StephanOtter
# Sound files downloaded initially as mp3. 
# Then converted to .wav using this website: https://audio.online-convert.com/convert-to-wav

# Be sure to change the bit resolution to "16 bit", sampling rate to "8000 Hz" & the audio channels to "mono" or "1 channel"

"""Make Vector drive straight and beep like R2-D2.

Make Vector beep like R2-D2, drive straight for 70 cm and then screen like R2-D2.
"""


import anki_vector
from anki_vector.util import degrees, distance_mm, speed_mmps


def main():
    args = anki_vector.util.parse_command_args()

    # The robot drives straight, stops and then turns around
    with anki_vector.Robot(args.serial) as robot:
        robot.audio.stream_wav_file("1.wav", 75)
        robot.behavior.drive_off_charger()

        # Use a "for loop" to repeat the indented code 4 times
        # Note: the _ variable name can be used when you don't need the value
        for _ in range(4):
            print("Drive Vector straight...")
            robot.behavior.drive_straight(distance_mm(700), speed_mmps(200))


        robot.audio.stream_wav_file("3.wav", 75)

if __name__ == "__main__":
    main()
