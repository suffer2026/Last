@echo off

echo Removing old output...
cmd /c hdfs dfs -rm -r /output >nul 2>nul

echo Copying input files...
cmd /c hdfs dfs -mkdir -p /user/input/
cmd /c hdfs dfs -put titanic.csv /user/input/titanic.csv

echo Setting file permissions
cmd /c icacls *.py /grant %USERNAME%:R

echo.
echo Running Hadoop Titanic Analysis...

cmd /c hadoop jar "%HADOOP_HOME%\..\share\hadoop\tools\lib\hadoop-streaming-3.2.4.jar" -input /user/input/titanic.csv -output /output -mapper "python mapper.py" -reducer "python reducer.py" -file mapper.py -file reducer.py 

echo.
echo ===== FINAL OUTPUT =====

cmd /c hdfs dfs -cat /output/part-00000

echo.
pause
