=================================
 Software Center Operator Manual
=================================

.. contents:: Table of Contents
.. sectnum::


Scope
=====

.. This section shall be divided into the following paragraphs.


Identification
--------------

.. This paragraph shall contain a full identification of the system
   and software to which this document applies, including, as
   applicable, identification number(s), title(s), abbreviation(s),
   version number(s), and release number(s).


System overview
---------------

.. This paragraph shall briefly state the purpose of the system and
   the software to which this document applies. It shall describe the
   general nature of the system and software; summarize the history of
   system development, operation, and maintenance; identify the
   project sponsor, acquirer, user, developer, and support agencies;
   identify current and planned operating sites; and list other
   relevant documents.


Document overview
-----------------

.. This paragraph shall summarize the purpose and contents of this
   manual and shall describe any security or privacy considerations
   associated with its use.


Referenced documents
====================

.. This section shall list the number, title, revision, and date of
   all documents referenced in this manual. This section shall also
   identify the source for all documents not available through normal
   Government stocking activities.


Software summary
================

.. This section shall be divided into the following paragraphs.


Software application
--------------------

.. This paragraph shall provide a brief description of the intended
   uses of the software. Capabilities, operating improvements, and
   benefits expected from its use shall be described.


Software inventory
------------------

.. This paragraph shall identify all software files, including
   databases and data files, that must be installed for the software
   to operate. The identification shall include security and privacy
   considerations for each file and identification of the software
   necessary to continue or resume operation in case of an emergency.


Software environment
--------------------

.. This paragraph shall identify the hardware, software, manual
   operations, and other resources needed to install and operate the
   software. Included, as applicable, shall be identification of:

.. Computer equipment that must be present, including amount of memory
   needed, amount of auxiliary storage needed, and peripheral
   equipment such as terminals, printers, and other input/output
   devices
   Communications equipment that must be present
   Other software that must be present, such as networking software,
   operating systems, databases, data files, utilities, permanent
   files that are referenced, created, or updated by the software; and
   databases/data files necessary to resume operation in the event of
   emergencies
   Forms, procedures, or other manual operations that must be present
   Other facilities, equipment, or resources that must be present

Software organization and overview of operation
-----------------------------------------------

.. This paragraph shall provide a brief description of the
   organization and operation of the software from the operator's
   point of view. The description shall include, as applicable:

.. Logical components of the software, from the operator's point of
   view, and an overview of the purpose/operation of each component
   Types of inputs/access that can be made to the software and the
   software's response to each type
   The reports and other outputs that are produced by the software,
   including security and privacy considerations for each
   Typical run times and factors that affect it
   Organization of software operation into runs. This description
   shall use a chart, if applicable, showing how the different
   operations are interrelated. If sets of runs are grouped by time
   periods or cycles, each set of integrated operations required on a
   daily, weekly, etc., basis shall be presented. If runs may be
   grouped logically by organizational level, the groups of runs that
   can be performed by each organizational level such as headquarters
   processing, field activity processing, etc., shall be presented.
   Any system restrictions, waivers of operational standards,
   information oriented toward specific support areas (for example,
   library, small computer and teleprocessing support, interfaces with
   other systems), or other special aspects of processing
   General description of the communications functions and processes
   of the software, including, as applicable, a diagram of the
   communications network used in the system

Contingencies and alternate states and modes of operation
---------------------------------------------------------

.. This paragraph shall explain the differences in software operation
   at times of emergency and in various states and modes of operation,
   if applicable.


Security and privacy
--------------------

.. This paragraph shall contain an overview of the security and
   privacy considerations associated with the software. A warning
   shall be included regarding making unauthorized copies of software
   or documents, if applicable.


Assistance and problem reporting
--------------------------------

.. This paragraph shall identify points of contact and procedures to
   be followed to obtain assistance and report problems encountered in
   operating the software.


Installation and setup
======================

.. This paragraph shall describe any procedures that the operator must
   perform to install the software on the equipment, to configure the
   software, to delete or overwrite former files or data, and to enter
   parameters for software operation. Safety precautions, marked by
   WARNING or CAUTION, shall be included where applicable.


Description of runs
===================

.. This section shall be divided into the following paragraphs to
   provide a description of the runs to be performed. Safety
   precautions, marked by WARNING or CAUTION, shall be included where
   applicable.


Run inventory
-------------

.. This paragraph shall provide a list of the runs to be performed,
   identifying the software and the jobs that make up each run. It
   shall include a brief summary of the purpose of each run and shall
   relate the list to the run descriptions included in the remainder
   of this section.


Phasing
-------

.. This paragraph shall describe acceptable phasing of the software
   into a logical series of operations. A run may be phased to permit
   manual or semiautomatic checking of intermediate results, to
   provide the user with intermediate results for other purposes, or
   to permit a logical break if higher priority jobs are submitted. An
   example of the minimum division for most systems would be edit,
   file update, and report preparation.


Diagnostic procedures
---------------------

.. This paragraph shall provide the setup and execution procedures for
   any software diagnostics. Included shall be procedures for
   validation and trouble shooting. All parameters (both input and
   output), codes, and range values for diagnostic software shall be
   explained.


Error messages
--------------

.. This paragraph shall list all error messages output by the
   software, along with the meaning and corresponding correction
   procedure for each message.


Description of each run
-----------------------

.. This paragraph shall be divided into the following subpara-graphs.


Run description for (run name or identifier)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. This paragraph shall identify a run and shall be divided into the
   following subparagraphs to describe the run.


Control inputs
++++++++++++++

.. This paragraph shall provide a listing of the run stream of job
   control statements needed to initiate the run.


Run management information
++++++++++++++++++++++++++

.. This paragraph shall provide the information needed to manage the
   run including, as applicable:

.. Peripheral and resource requirements
   Security and privacy considerations
   Method of initiation, such as on request, after another run, or at
   a predetermined time
   Estimated run time
   Required turnaround time
   Messages and responses
   Procedures for taking check points
   Waivers from operational standards

Input-output files
++++++++++++++++++

.. This paragraph shall provide information about the files and
   databases that serve as input to or that are created or updated by
   the run. Included for each shall be information such as name,
   security and privacy, recording medium, retention schedule, and
   disposition.


Output reports
++++++++++++++

.. This paragraph shall provide information about the reports that are
   produced during the run. In-cluded for each report shall be the
   following information, as applicable: report identifier, product
   control number, report control symbol, title, security and privacy,
   media (e.g., hard copy, magnetic tape), volume of report, number of
   copies, and distribution of copies.


Reproduced output reports
+++++++++++++++++++++++++

.. This paragraph shall provide information about computer-generated
   reports that are subse-quently reproduced by other means. Included
   for each report shall be information such as report identification,
   security and privacy, reproduction technique, paper size, binding
   method, number of copies, and distribution of copies.


Procedures for restart/recovery and continuity of operations
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. This paragraph shall provide procedures to be followed by operator
   personnel concerning re-start/recovery in the event of a system
   failure and for continuity of operations in the event of
   emergencies.


Notes
=====

.. This section shall contain any general information that aids in
   understanding this document (e.g., background information,
   glossary, rationale). This section shall include an alphabetical
   listing of all acronyms, abbreviations, and their meanings as used
   in this document and a list of terms and definitions needed to
   understand this document.


Appendixes
==========

.. Appendixes may be used to provide information published separately
   for convenience in document maintenance (e.g., charts, classified
   data). As applicable, each appendix shall be referenced in the main
   body of the document where the data would normally have been
   provided. Appendixes may be bound as separate documents for ease in
   handling. Appendixes shall be lettered alphabetically (A, B,
   etc.).



