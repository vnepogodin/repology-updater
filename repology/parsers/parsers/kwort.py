# Copyright (C) 2019 Dmitry Marakasov <amdmi3@amdmi3.ru>
#
# This file is part of repology
#
# repology is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# repology is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with repology.  If not, see <http://www.gnu.org/licenses/>.

from typing import Iterable

from repology.packagemaker import NameType, PackageFactory, PackageMaker
from repology.parsers import Parser
from repology.parsers.sqlite import iter_sqlite


class KwortKdbParser(Parser):
    def iter_parse(self, path: str, factory: PackageFactory) -> Iterable[PackageMaker]:
        for pkgdata in iter_sqlite(path, 'MIRRORPKG', ['NAME', 'VERSION', 'ARCH']):
            with factory.begin() as pkg:
                pkg.add_name(pkgdata['NAME'], NameType.KWORT_NAME)
                pkg.set_version(pkgdata['VERSION'])
                pkg.set_arch(pkgdata['ARCH'])

                yield pkg
