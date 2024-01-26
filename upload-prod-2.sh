
expect -c "
spawn scp ../article_spider.zip root@8.210.126.239:/home/freedomproject/article_spider.zip

expect {
    \"*assword\"
                {
                    set timeout 300;
                    send \"Xianyadan123.\r\";
                }
    \"yes/no\"
                {
                    send \"yes\r\"; exp_continue;}
                }
expect eof"