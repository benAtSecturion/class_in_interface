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

test.compile(
    verilator_flags2=['--binary', '--stats', '-fno-dfg', '-CFLAGS "-Wno-overloaded-virtual"'])

test.execute()

<<<<<<< HEAD
test.file_grep(test.stats, r'Scheduling, Timing, variables written by suspendables\s+(\d+)', 11)
test.file_grep(test.stats, r'Scheduling, Timing, external sensitivities, total\s+(\d+)', 11)
test.file_grep(test.stats, r'Scheduling, Timing, unique external sentrees\s+(\d+)', 1)
=======
test.file_grep(test.stats,
<<<<<<< HEAD
               r'Scheduling, count of non-inlined signal writes in suspendables\s+(\d+)', 14)
>>>>>>> 026c2f227 (code fixes)
=======
               r'Scheduling, count of non-inlined signal writes in suspendables\s+(\d+)', 8)
>>>>>>> e6e73f40b (hopefully fixed t_sched_noninlined_func_suspendable2)

test.passes()
