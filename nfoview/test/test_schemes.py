# Copyright (C) 2008-2009 Osmo Salomaa
#
# This file is part of NFO Viewer.
#
# NFO Viewer is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# NFO Viewer is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# NFO Viewer. If not, see <http://www.gnu.org/licenses/>.

import nfoview


class  _TestScheme(nfoview.TestCase):

    def setup_method(self, method):
        self.scheme = None
        raise NotImplementedError

    def test_attributes(self):
        assert hasattr(self.scheme, "name")
        assert hasattr(self.scheme, "label")
        assert hasattr(self.scheme, "foreground")
        assert hasattr(self.scheme, "background")
        assert hasattr(self.scheme, "link")
        assert hasattr(self.scheme, "visited_link")


class TestBlackOnWhiteScheme(_TestScheme):

    def setup_method(self, method):
        self.scheme = nfoview.BlackOnWhiteScheme


class TestCustomScheme(_TestScheme):

    def setup_method(self, method):
        self.scheme = nfoview.CustomScheme


class TestDarkGreyOnLightGrayScheme(_TestScheme):

    def setup_method(self, method):
        self.scheme = nfoview.DarkGreyOnLightGrayScheme


class TestDefaultScheme(_TestScheme):

    def setup_method(self, method):
        self.scheme = nfoview.DefaultScheme


class TestGreyOnBlackScheme(_TestScheme):

    def setup_method(self, method):
        self.scheme = nfoview.GreyOnBlackScheme


class TestLightGreyOnDarkGrayScheme(_TestScheme):

    def setup_method(self, method):
        self.scheme = nfoview.LightGreyOnDarkGrayScheme


class TestWhiteOnBlackScheme(_TestScheme):

    def setup_method(self, method):
        self.scheme = nfoview.WhiteOnBlackScheme
