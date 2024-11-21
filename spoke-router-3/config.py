#!/usr/bin/python

# Copyright (C) 2019 strangebit

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

config = {
    "public_ip": "1.1.1.6",
    "private_ip": "192.168.3.2",
    "hub_ip": "1.1.1.4",
    "public_interface": "r6-eth1",
    "private_interface": "r6-tun1",
    "enable_auth": True,
    "hip": [
        {
            "src": "1.1.1.6",
            "dst": "1.1.1.10",
            "ihit": "2001:0021:d666:2c04:242f:e2b4:cbe7:b3b3",
            "rhit": "2001:0021:b4b6:b7a4:f4cc:0f6b:8779:8ef9"
        }
    ]
}
