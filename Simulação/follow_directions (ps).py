import argparse
import json
import os
from os.path import abspath, dirname
from time import sleep
from typing import List, NamedTuple, cast

import airsim

print_verbose = lambda *args, **kwargs: print(*args, **kwargs)


class Direction(NamedTuple):
    steering: float
    throttle: float
    duration: float  # in seconds


def do_brake(client: airsim.CarClient, intensity: float = 1.0) -> None:
    client.setCarControls(
        airsim.CarControls(0.0, 0.0, max(0.0, min(intensity, 1.0)), True)
    )


def do_drive(client: airsim.CarClient, steering: float, throttle: float) -> None:
    client.setCarControls(
        airsim.CarControls(max(0.0, min(throttle, 1.0)), steering, 0.0, False)
    )


### setup (called before connecting) ###########################################
def setup(directions: str) -> List[Direction]:
    print_verbose("Hi, I'm just setting up...")

    # TODO parse directions into a list of Direction...


### drive (called after connecting) ############################################
def drive(client: airsim.CarClient, direction_list: List[Direction]) -> None:
    print_verbose("Ready, let's drive!")

    client.reset()

    # TODO follow the Direction list...

    (image_response,) = cast(
        List[airsim.ImageResponse],
        client.simGetImages(
            requests=[airsim.ImageRequest("front_center", airsim.ImageType.Scene)]
        ),
    )

    airsim.write_file(
        os.path.join(dirname(abspath(__file__)), "triangle.png"),
        image_response.image_data_uint8,
    )


### main #######################################################################
def main(directions: str) -> None:
    print_verbose(airsim.__path__)

    direction_list = setup(directions)

    # TODO connect a client to AirSim...

    try:
        drive(client, direction_list)
    except KeyboardInterrupt:
        client.reset()
    finally:
        print("And... we're done!")


################################################################################
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Drive a car through a given set of directions."
    )

    parser.add_argument(
        "--directions",
        type=str,
        default=os.path.join(dirname(abspath(__file__)), "directions.json"),
        help="path to a JSON file with directions  (default: %(default)s)",
    )
    parser.add_argument(
        "--no_verbose",
        "-n",
        action="store_true",
        help="decrease output message verbosity",
    )

    args = parser.parse_args()

    if args.no_verbose:
        print_verbose = lambda *args, **kwargs: None

    with open(args.directions, "r") as f:
        directions = f.read()

    main(directions)
