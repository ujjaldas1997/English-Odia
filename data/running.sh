x=1
while [ $x -gt 0 ]
do
    python data_extract.py
    x=$?
done
