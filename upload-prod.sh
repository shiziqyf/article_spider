
expect -c "
spawn scp ../article_spider.zip root@***:/home/freedomproject/article_spider.zip

expect {
    \"*assword\"
                {
                    set timeout 300;
                    send \"***\r\";
                }
    \"yes/no\"
                {
                    send \"yes\r\"; exp_continue;}
                }
expect eof"