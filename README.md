gitcheck
========

Reports counts of modified and untracked files in all git directories within a
passed directory. 

    positional arguments:
	    dir            directory to check

    optional arguments:
      -h, --help     show this help message and exit
      -v, --verbose  show all git statuses (default is only directories with
                 modified files)
      -a, --abspath  show absolute path to directory (default is relative path to dir)


Install
-------

gitcheck depends on the `sh` Python module, which is a wrapper for subprocess. 
You can install this with `pip` or `easy_install`.
Once that's complete, run: 

    git clone git@github.com:johnjosephhorton/gitcheck.git
	cd gitcheck
	sudo python setup.py install 
	
Example
-------
Suppose I have single untracked file in my repository and a single modified file in `~/john_stuff_lazy` and a fully up-to-date repository in `~/john_stuff`. 

    $ gitcheck ~ 
	1 1 ./john_stuf_lazy 
	
	$ gitcheck ~ -v
	1 1 ./john_stuf_lazy 
    0 0 ./john_stuf
	
	$ gitcheck ~ -va
	1 1 /home/john/john_stuf_lazy 
    0 0 /home/john/john_stuf
	
	
	
	



