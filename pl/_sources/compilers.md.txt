---
sd_hide_title: true
...

<p style="text-align: center;font-size:36px;color:#734f96;"><b>Fortran Compilers</b></p>
<p style="text-align: center;font-size:24px;">Fortran has over a dozen open source and commercial compilers.</p>

## Compilers

<p style="font-size:24px;color:#734f96;"><b>Open source compilers</b></p>

<h4> <b> GNU Fortran Compiler</b></h4>

[GNU Fortran Compiler (gfortran)](https://gcc.gnu.org/fortran/) is a mature
compiler, part of the GNU Compiler Collection.

*Free and open source under
[GNU General Public License](https://gcc.gnu.org/onlinedocs/gcc-4.2.4/gfortran/Copying.html#Copying).*

[OpenCoarrays](http://www.opencoarrays.org/) is a library and compiler wrapper
around gfortran which enables the parallel programming features of Fortran 2018
with gfortran.

*Free and open source under
[BSD-3 license](https://github.com/sourceryinstitute/OpenCoarrays/blob/main/LICENSE).*

<h4> <b> LLVM Flang</b></h4>

[Flang](https://github.com/llvm/llvm-project/tree/main/flang)
is a new front-end for Fortran 2018 that has been recently
added to LLVM.
It is implemented in modern C++ and uses a Fortran-oriented MLIR dialect for lowering to LLVM IR.
This project is under active development.

*Free and open source under
[Apache License v2.0 with LLVM Exceptions](https://github.com/llvm/llvm-project/blob/main/flang/LICENSE.TXT).*

<h4> <b> Current Flang</b></h4>

[Flang](https://github.com/flang-compiler/flang) is a compiler based on the
NVIDIA/PGI commercial compiler.

*Free and open source under
[Apache License v2.0 with LLVM Exceptions](https://github.com/flang-compiler/flang/blob/master/LICENSE.txt).*

<h4> <b> LFortran </b></h4>

[LFortran](https://lfortran.org) is a modern, interactive, LLVM-based Fortran
compiler.
Also available online at [dev.lfortran.org](https://dev.lfortran.org/) using a statically served, WASM based LFortran Compiler for running code in web browsers.

*Free and open source under
[BSD-3 license](https://github.com/lfortran/lfortran/blob/main/LICENSE).*

<p style="font-size:24px;color:#734f96;"><b>Commercial compilers</b></p>

<h4> <b> Intel oneAPI</b></h4>

[Intel oneAPI](https://software.intel.com/content/www/us/en/develop/tools/oneapi/all-toolkits.html)
is Intel's suite of compilers, tools, and libraries for Fortran, C, C++, and
Python. Intel oneAPI HPC Toolkit provides
[two Fortran compilers](https://software.intel.com/content/www/us/en/develop/articles/intel-oneapi-fortran-compiler-release-notes.html):

- Intel Fortran Compiler (`ifx`), a new, LLVM-based compiler
  that comes with full Fortran 2018 support. It also supports the [majority of OpenMP 5.0/5.1](https://www.intel.com/content/www/us/en/developer/articles/technical/fortran-language-and-openmp-features-in-ifx.html) including offload to Intel GPUs. 
  ifx can also offload `do concurrent` to Intel GPUs.
- Intel Fortran Compiler Classic (`ifort`), a mature compiler
  with full Fortran 2018 support, for CPUs only.

Currently the ifx compiler supports Linux and Windows platforms for x86-64 architectures. ifort supports Linux, Windows, and macOS.

*The current version of Intel oneAPI is
[available for free](https://www.intel.com/content/www/us/en/developer/articles/tool/oneapi-standalone-components.html),
and support can be purchased.
Community support is available for the free version at the [Intel Developer forum](https://community.intel.com/t5/Intel-Fortran-Compiler/bd-p/fortran-compiler).
Optionally, you can purchase [Priority Support](https://www.intel.com/content/www/us/en/developer/get-help/priority-support.html) with additional benefits including access to previous versions of ifort and ifx.
For licensing information related to Intel oneAPI, see the
[Intel End-User License Agreement](https://www.intel.com/content/www/us/en/developer/articles/license/end-user-license-agreement.html)*.

<h4> <b> NAG </b></h4>

The latest [NAG Fortran Compiler](https://nag.com/nag-compiler)
release (7.0) has extensive support for legacy and modern Fortran features including parallel programming with coarrays, as well as additional support for programming with OpenMP.

The Compiler also provides significant support for Fortran 2018 (atomic
operations, events and tasks, plus other smaller features), almost all of
Fortran 2008, complete coverage of Fortran 2003, and all of OpenMP 3.1. All
platforms include supporting tools for software development: source file
polishers, dependency generator for module and include files, call-graph
generator, interface builder and a precision unifier.

*Purchasable from the [NAG website](https://nag.com/buy-now/) under the
[NAG software license](https://support.nag.com/termsandconditions/nag-software-licence-t-and-c.pdf)*

<h4> <b> NVIDIA</b></h4>

The [NVIDIA HPC SDK](https://developer.nvidia.com/hpc-sdk) C, C++, and Fortran compilers, former [PGI compilers](https://www.pgroup.com/products/index.htm), support GPU acceleration of HPC modeling and simulation applications with standard C++ and Fortran, OpenACC® directives, and CUDA®. GPU-accelerated math libraries maximize performance on common HPC algorithms, and optimized communications libraries enable standards-based multi-GPU and scalable systems programming.

Currently the compiler supports Linux platforms and x86_64, ppc64le and aarch64 architectures.
Community support is available at the [HPC compiler forum](https://forums.developer.nvidia.com/c/accelerated-computing/hpc-compilers/nvc-nvc-and-nvfortran/313).

*[Freely available](https://developer.nvidia.com/hpc-sdk-downloads) under
[NVIDIA Software License Agreement](https://docs.nvidia.com/hpc-sdk/eula/index.html).*

<h4> <b> HPE / Cray</b></h4>

The [Cray Compiling Environment (CCE)](https://developer.hpe.com/platform/hpe-cray-programming-environment/home/)
is the cornerstone innovation of Cray's adaptive computing paradigm. CCE builds
on a well-developed and sophisticated Cray technology base that identifies
regions of computation that are either sequential scalar, vector parallel or
highly multithreaded. It includes optimizing compilers that automatically
exploit the scalar, vector and multithreading hardware capabilities of the Cray
system. CCE supports Fortran, C and C++.

*Purchasable from
[HPC Support Center](https://support.hpe.com/connect/s/product) under HPE
License Terms.*

<h4> <b> IBM </b></h4>

[IBM® XL Fortran](https://www.ibm.com/us-en/marketplace/xl-fortran-linux-compiler-power)
for Linux is an industry standards-based programming tool used to develop large
and complex applications in the Fortran programming language. It generates code
that leverages the capabilities of the latest POWER9 architecture and maximizes
your hardware utilization. IBM XL Fortran for Linux optimizes your
infrastructure on IBM Power Systems™ in support of extensive numerical,
scientific and high-performance computing.

The compilers support Linux and AIX platforms and ppc64le architectures.

*Purchasable from the
[IBM website](https://www.ibm.com/products/fortran-compiler-family) under the
relevant
[IBM License Agreement](https://www.ibm.com/about/software-licensing/us-en). A
[community edition](https://www.ibm.com/products/open-xl-fortran-linux-compiler-power)
of the IBM XL compilers are available free of charge.*

<h4> <b> AMD </b></h4>

The [AMD Optimizing C/C++ Compiler (AOCC)](https://developer.amd.com/amd-aocc/)
compiler system is a high performance, production quality code generation tool.
The AOCC environment provides various options to developers when building and
optimizing C, C++, and Fortran applications targeting 32-bit and 64-bit Linux®
platforms. The AOCC compiler system offers a high level of advanced
optimizations, multi-threading and processor support that includes global
optimization, vectorization, inter-procedural analyses, loop transformations,
and code generation. AMD also provides highly optimized libraries, which extract
the optimal performance from each x86 processor core when utilized. The AOCC
Compiler Suite simplifies and accelerates development and tuning for x86
applications.

The AOCC compilers are available free of charge and support Linux platforms with x86_64 architectures.

*Freely available on the
[AMD website](https://www.amd.com/en/developer/aocc.html) under the
[AMD AOCC End-User License Agreement](https://www.amd.com/en/developer/aocc/aocc-compiler/eula.html).*

<h4> <b> ARM </b></h4>

[Arm Fortran compiler for Linux](https://developer.arm.com/Tools%20and%20Software/Arm%20Fortran%20Compiler).
Tailored for HPC and scientific codes, with support for popular Fortran and
OpenMP standards and tuned for leading server-class Arm-based platforms. Built
on the open source Flang front-end, and the LLVM‑based optimization and code
generation back-end. Available as part of the Arm Compiler for Linux package.

*Freely available on the
[Arm website](https://developer.arm.com/documentation/102621/0100/Download?lang=en) under the
[License agreement](https://developer.arm.com/documentation/102621/0100).*

<h4> <b> Oracle / Sun </b></h4>

[Oracle C, C++, Fortran Compiler](https://www.oracle.com/application-development/technologies/developerstudio-features.html)
is highly optimized for Oracle systems, on-premise and in the cloud.

- Advanced code generation technology for the latest Oracle SPARC and x86 based systems.
- Support for the latest industry standards, including C++14, C++11, C11 and OpenMP 4.0 and extensive GCC compatibility features.
- Automatic code analysis during compilation and automatic stack overflow protection at application runtime.

*Purchasable from the
[Oracle website](https://www.oracle.com/application-development/technologies/developerstudio.html)
under the
[Oracle License and Services Agreement](https://www.oracle.com/us/corporate/pricing/olsa-ire-v122304-070683.pdf).*

<h4> <b> Silverfrost FTN95 </b></h4>

[Silverfrost FTN95](https://www.silverfrost.com/) is a full Fortran 95 standards
compliant compiler, capable of producing fast executables for Win32 and for
Microsoft .NET. FTN95 ships with the world's best runtime checking and a great
range of supporting software. All standard and many vendor-specific legacy
language features are supported, so that Fortran projects may be any combination
of Fortran 77, Fortran 90 and Fortran 95.
Some features of Fortran 2003 and 2008 have been [added](https://www.silverfrost.com/19/ftn95/support/ftn95_revision_history.aspx).
Silverfrost Fortran runs on Windows / x86_64.

*Purchasable from the
[Silverfrost website](https://www.silverfrost.com/P1001/shop/silverfrost_ftn95.aspx)
(there is also a
[free personal edition](https://www.silverfrost.com/32/ftn95/ftn95_personal_edition.aspx)
under the
[Silverfrost Fortran FTN95 License Agreement](https://www.silverfrost.com/44/ftn95/ftn95_licence_options.aspx)*.

<h4> <b> NEC </b></h4>

[The Fortran compiler](https://www.nec.com/en/global/solutions/hpc/sx/tools.html)
conforms to the Fortran-2003 standard (ISO/IEC 1539-1:2004) and supports many
features from Fortran-2008 (ISO/IEC 1539-1:2010).

*Freely available from the
[community repository](https://sxauroratsubasa.sakura.ne.jp/repos/community/sdk/)
(see [blog post](https://sx-aurora.github.io/posts/nec-compilers-no-license/)
for more information) under the
[SX-Aurora TSUBASA Free Software License](https://sxauroratsubasa.sakura.ne.jp/documents/support/pdfs/AuroraSW_Free_List.pdf).*

<h4> <b> LCC </b></h4>

[MCST C, C++, Fortran Compiler](http://mcst.ru/lcc) with full support of Fortran-95
(ISO/IEC 1539:1997) and partial support of Fortran-2003 (ISO/IEC 1539:2004),
Fortran-2008 (ISO/IEC 1539:2010) and Fortran-2018 (ISO/IEC 1539:2018). Used for
Russian processor architectures Elbrus (e2k) and SPARC (MCST-R), also a
cross-compiler for x86_64 architecture is available.

<h3> Discontinued </h3>

The following is a list of Fortran compilers that seem discontinued, so we do
not list them above:

- Absoft
- Apogee
- Edinburgh Portable Compilers
- Hewlett Packard
- Lahey
- Watcom
- PathScale
- G95
- Open64
- Unisys

<h3> Note </h3>

Please let us know if there is any compiler that is not listed, or if we listed
a compiler in the Discontinued section and it is in fact actively maintained.
