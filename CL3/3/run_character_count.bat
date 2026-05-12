@echo off

echo Removing old output...
cmd /c hdfs dfs -rm -r /output >nul 2>nul

echo Copying input files...
cmd /c hdfs dfs -mkdir -p /user/input/
cmd /c hdfs dfs -put input.txt /user/input/input.txt

echo Setting file permissions
cmd /c icacls *.py /grant %USERNAME%:R

echo.
echo Running Hadoop Character Count...

cmd /c hadoop jar "%HADOOP_HOME%\..\share\hadoop\tools\lib\hadoop-streaming-3.2.4.jar" -input /user/input/input.txt -output /output -mapper "python char_mapper.py" -reducer "python char_reducer.py" -file char_mapper.py -file char_reducer.py 

echo.
echo ===== FINAL OUTPUT =====

cmd /c hdfs dfs -cat /output/part-00000

echo.
pause
