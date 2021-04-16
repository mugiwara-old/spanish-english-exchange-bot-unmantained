# spanishenglishexchange.com (bot)

spanishenglishexchange.com (bot) is a lovely bot to improve user experience on our discord server.

## To-do
- [ ] Update changelog
- [ ] Creat a cron/task for the counter funct

## Installation (using conda)

Clone repo, then cd path/to/repo 

```bash
conda create -y --name py39 python=3.9
conda install -c conda-forge --file requirements.txt
conda activate py39
```

## Usage

```bash
python main.py
```
Notice that you'll need to create an .env file with your API KEYS plus you should modifiy "Guild" class with your roles & channels :)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
