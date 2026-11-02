#!/usr/bin/env python3
# DESCRIPTION: Verilator: Verilog Test driver/expect definition
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of either the GNU Lesser General Public License Version 3
# or the Perl Artistic License Version 2.0.
# SPDX-FileCopyrightText: 2026 Wilson Snyder
# SPDX-License-Identifier: LGPL-3.0-only OR Artistic-2.0

import vltest_bootstrap

test.scenarios('simulator')

test.compile(verilator_flags2=['--binary', '--stats', '-fno-dfg','-CFLAGS "-Wno-overloaded-virtual"'])

test.execute()

<<<<<<< HEAD
test.file_grep(test.stats, r'Scheduling, Timing, variables written by suspendables\s+(\d+)', 8)
test.file_grep(test.stats, r'Scheduling, Timing, external sensitivities, total\s+(\d+)', 8)
test.file_grep(test.stats, r'Scheduling, Timing, unique external sentrees\s+(\d+)', 1)
=======
test.file_grep(test.stats,
               r'Scheduling, count of non-inlined signal writes in suspendables\s+(\d+)', 11)
>>>>>>> 0721036d4 (added compiler flags and white space fixes)

test.passes()
