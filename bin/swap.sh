#/bin/bash

installmgr -u Packard
oldzip=/home/melmoth/dev/packard/packard.zip

rm -rf ./tmp
mkdir ./tmp

if [ $1 = "devel" ]  
then
 echo "devel";
 cp packard.conf $SWORD_PATH/mods.d
 cp -r packard/ $SWORD_PATH/modules/lexdict/zld/
else
 echo "standard";
 #cp $oldzip ./tmp
 #cd tmp
 #unzip LXX.zip
 #cp mods.d/lxx.conf $SWORD_PATH/mods.d
 #mv modules/texts/ztext/lxx/ $SWORD_PATH/modules/texts/ztext
fi 

