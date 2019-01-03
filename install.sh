UNAME=$(uname | tr "[:upper:]" "[:lower:]")
if [ "$UNAME" = "linux" ]; then
    # If available, use LSB to identify distribution
    if [ -f /etc/lsb-release -o -d /etc/lsb-release.d ]; then
        distro=$(lsb_release -i | cut -d: -f2 | sed s/'^\t'//)
    # Otherwise, use release info file
    else
        distro=$(ls -d /etc/[A-Za-z]*[_-][rv]e[lr]* | grep -v "lsb" | cut -d'/' -f3 | cut -d'-' -f1 | cut -d'_' -f1)
   fi
fi
echo "$distro"
[ "$distro" = "" ] && distro=$UNAME
echo "${distro,,}"
if [[ "${distro}" = *"ubuntu"* ]];then
    echo "eeee"
fi
