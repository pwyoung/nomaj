# Goal

Show how to access nomaj


# Instructions

## Put the following in your login script (e.g. ~/.bash_profile)

echo "Set up nomaj"
NOMAJ_HOME=/home/$USER/git/nomaj
if [ -e $NOMAJ_HOME ]; then
    export PATH=$PATH:$NOMAJ_HOME
fi

# Support "cd $NOMAJ_HOME"
export $NOMAJ_HOME
