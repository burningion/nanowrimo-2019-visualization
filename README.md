# NaNoWriMo 2019 Visualization

![NaNoWriMo Visualization](https://github.com/burningion/nanowrimo-2019-visualization/raw/master/images/chart.png)

In November of 2019, I participated in NaNoWriMo. It's a chance to commit to 30 days of writing at least 1667 words per day. 

I had a few missed days, but this is a chart of my efforts, generated with the `generate_chart.py` file attached.

For each day, I created a `00.md` file, and wrote the day's efforts. This year, I missed two days, and made up for it with extra effort in other days.

I used the Linux utility `wc`, or wordcount, to keep track of my total word count. You'll see in the code how the words are counted:

```python
import glob

days = {} 

# first, count the number of words in every md file
for filename in glob.glob('*.md'):
    processname = f"wc -w {filename}".split()
    process = subprocess.Popen(processname, stdout=subprocess.PIPE)
    for line in process.stdout:
        if b"the" in line:
            continue
        days[int(filename[:2])] = int(line.decode('utf-8').split()[0])
```
