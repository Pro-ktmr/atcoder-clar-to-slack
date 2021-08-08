#!/usr/bin/env python3

import time, yaml
import atcoder as ac
import slack as sl

def load_config():
    with open('config.yml', 'r') as f:
        return yaml.load(f, Loader = yaml.FullLoader)

def main():
    config = load_config()
    atcoder = ac.Atcoder()
    atcoder.login(config['USERNAME'], config['PASSWORD'])
    slack = sl.Slack()

    clars = atcoder.load_clar_page(config['CLAR_URL'])
    while True:
        current_clars = atcoder.load_clar_page(config['CLAR_URL'])
        for i in range(len(current_clars)):
            if i >= len(clars) or clars[i] != current_clars[i]:
                slack.send_message(config['SLACK_URL'],
                                   current_clars[i].convert_json(i < len(clars)))
        clars = current_clars
        time.sleep(config['INTERVAL'])

if __name__ == "__main__":
    main()