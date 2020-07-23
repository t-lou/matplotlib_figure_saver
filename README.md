# **Pytena** executes python scripts and saves matplotlib images

When we use python to investigate data and processing, it sucks to have the results in png or svg. Zooming and cutting are not well supported, the real time ruler in plt.show is also helpful.

This small program makes it possible to save and load matplotlib images easily, and provides simple execution by selecting python scripts and typing python statements (like spyder).

# Start

```bash
python main.py
```

# Idea

The figures will be saved with pickle (instead of cPickle for compatibility) and '.pmg' as extension (portable matplotlib graph). Before the plots are shown, use the predefined functions to save them. The predefined functions are described in help entry.

There is an entry to load the saved images in the main menu. As pmg contains the cached data from matplotlib, one file can contain multiple images.

# Main entries

- **Script** select a python script to execute
- **Image** display one pmg file containing one or more images
- **Command** open one text editor for interactive execution
- **Help** show the predefiend functions
