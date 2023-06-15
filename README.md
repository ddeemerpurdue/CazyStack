### Welcome to CazyStack
# The Stackable Cazyme analysis toolkit
# TurboDog
<hr/>

**Objective:** To create a comprehensive toolkit that allows the scalable, reproducible, and efficient analysis of CAZyme data to later be plugged into a larger network of data tools. 
<hr/>
> Problem Statement: Current tools are built on the analytic framework of input --> [computations] --> output. This will be referred to as the ICO framework. Often times log files are created in order to track which computations were performed on what files and what the output is representing. This collection of flat input, log, and output files remain connected only insofar as their relational paths to one another, as well as the textual descriptions found in log files. Often times files are moved across a filesystem, disconnecting the frail link between all files in the collection. When this collection of positioned files gets moved, modified, or deleted, a loss of data provenance occurs and the computation can no longer be completely validated. When files get modified by users the logging mechanisms of analysis tools of this analytical framework are unable to detect these changes and immediate loss of data provenance occurs at the **tool** level, meaning the user must track these changes and amend the log file/electronic notebook.  
> Further, analysis tools of this framework result in disconnected data output when replicating analyses or running new data through the tool. In order to compare data ran separately through these tools, researchers often times need to use custom scripts and data analysis workflows in order to compile all the data in a way to be properly compared. 
> 
<hr/>
**Solution:**  To create an interconnected data network across similar collections of data types and compute processes. The implementation utilizes a database management system (DBMS) + API in order to i) structure output in a scalable and efficient way, ii) track all analysis events internally through the database to ensure data provenance and iii) provide a data schema and storage platform that allows 'stackable data analysis'. Communication with all input, program, and output data will be done through a wrapper API connected to the MongoDB-hosted database (which can live on any local machine) with internal event logging. This wrapper also contains bult-in functionality for compiling data to analyze various levels based on metadata attributes. This allows data to be stored and analyzed beyond the researcher + project level, as different individuals within a group can share the same database and have the ability to query/analyze their isolated data or have it pre-compiled based on any provided metadata attribute(s).  
Note: Users will still have the ability to export all flat files and data, as well as perform all database interaction steps through MongoDB's native support.
<hr/>


**Vocabulary**  
1. Input-Computation-Output (ICO) framework  
2. Stackable data structure  
3. Data provenance  
4. Analysis workflow  
5. MongoDB  
6. DAta NEtwork (DANE)  
7. Pass