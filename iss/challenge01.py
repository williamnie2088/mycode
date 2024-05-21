#!/usr/bin/python3
"""Alta3 Research - astros on ISS"""

import urllib.request
import json

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    """reading json from api"""
    # call the api
    groundctrl = urllib.request.urlopen(MAJORTOM)

    # strip off the attachment (JSON) and read it
    # the problem here, is that it will read out as a string
    helmet = groundctrl.read()

    helmetson = json.loads(helmet.decode("utf-8"))

    print(f"People in space: {helmetson['number']}")

    # display every item in a list
    for astro in helmetson["people"]:
        # display what astro is
        print(f"{astro['name']} on the {astro['craft']}")


if __name__ == "__main__":
    main()

