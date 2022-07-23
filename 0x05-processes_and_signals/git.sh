#!/bin/bash
sudo chmod u+x *
git add .
echo "commit message"
read msg
git commit -m $msg
git push
