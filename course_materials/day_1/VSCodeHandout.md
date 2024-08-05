# Visual Studio code handout

Last Revised on August 4th, 2024

## Introduction

This handout is intended to assist participants of the Introductory
Python course offered by the Blind Information Technology Specialists
(BITS) in getting started with the Visual Studio Code (VSCode) editor.

## What is VSCode?

Visual Studio Code is an editor, a software application that enables one
to develop, or write computer programs. Code is the term programmers use
to describe the text of a programming language.

Visual Studio Code is called VSCode for short, and this term will be
used throughout this document. This tutorial is based on version 1.86 of
VSCode, current, February, 2024.

## Assumptions

This tutorial assumes you are comfortable with your access technology,
speech-enabled screen reader, magnification and/or Braille display. It
also assumes your visual impairment is severe enough that you depend on
access technology to work efficiently. It assumes you have little or no
programming experience.


## Configure Line Indentation Reporting for VoiceOver on macOS

### Global Configuration 

The following steps will guide you through enabling this setting globally. Skip down to find instructions on how this feature can be configured to only apply in certain contexts (e.g., when you are programming).
1. Navigate to the *VoiceOver Utility* by searching for it in Spotlight, LaunchPad, or if VoiceOver is enabled, use the keyboard command `control + option + F8`. If you have set your VO key to caps-lock, then hit `caps-lock + F8` instead.
2. Navigate to the *Verbosity* section. It is between the *General* and *Speech* sections. 
3. Navigate to the *Text* tab. It is the third tab between *Braille* and *Announcements*.
4. Locate the option named *Line Indentation*. The option will be between the *repeated spaces* and *while typing speak* options.
5. Switch from *Do Nothing* to your preferred method of receiving an indication of line indentation. It may be best to open a text editor or VSCode here and test while alternating between the available options to find the one that is best for you.
6. From the same dropdown for this option, select *Customize Level...* and ensure *Default Number of Spaces per Indent* is set to *4*. 

### Using an Activity

These instructions walk you through creating a VoiceOver Activity, assigning it to an app, and configuring the verbosity to report line indentation.
1. Navigate to the *VoiceOver Utility* by searching for it in Spotlight, LaunchPad, or if VoiceOver is enabled, use the keyboard command `control + option + F8`. If you have set your VO key to caps-lock, then hit `caps-lock + F8` instead.
2. Navigate to the *Activities* section. It is between the *Braille* and *VoiceOver Recognition* sections.
3. Find and click the option to *add activity*. Name it something that will help you identify it (e.g., Programming).
4. Under *settings to apply for this activity*, check *Verbosity*.
5. Under *automatically switch to this activity for*, locate the option *apps and websites* and from the dropdown, select VSCode.
6. Head back to the options under *settings to apply for this activity*, and choose the *Set...* button for *verbosity*.
7. Navigate to the *Text* tab. It is the third tab between *Braille* and *Announcements*.
8. Locate the option named *Line Indentation*. The option will be between the *repeated spaces* and *while typing speak* options.
9. Switch from *Do Nothing* to your preferred method of receiving an indication of line indentation. It may be best to open a text editor or VSCode here and test while alternating between the available options to find the one that is best for you.
10. From the same dropdown for this option, select *Customize Level...* and ensure *Default Number of Spaces per Indent* is set to *4*.
11. Select *Done* to save your changes.
12. Launch VSCode and open a file to test. The activity should have been automatically enabled by VoiceOver and the line indentation reporting setting you defined should be working. 

To confirm the activity you are in, and switch activities manually, use VoiceOver's *Activity Chooser*. Here are some instructions:
1. To bring up the *Activity Chooser*, hit the keyboard shortcut `control + option + X`. 
2. Navigate the *Activity Chooser* with the up and down arrow keys. From this menu, you will be able to identify the activity you are currently in, the one most recent activity you were previously in, and a list of any other activities including the default *VoiceOver settings* which is for the global VoiceOver settings. 
3. Use the enter key to switch to the highlighted activity, or escape to close out of the *Activity Chooser*.
4. If you want to quickly switch to the previously set activity manually, you can hit the keyboard shortcut `control + option + X X` (i.e., hold down `control + option` and tap `X` twice in quick succession.)


## Configuring Indentation for NVDA

Open Document Formatting Settings in NVDA with the hotkey
NVDA+control+d. Most of the options in this category are for configuring
what type of formatting you wish to have reported as you move the cursor
around documents.

### Line indentation reporting

This option allows you to configure how indentation at the beginning of
lines is reported. The Report line indentation with combo box has four
options.

-   Off: NVDA will not treat indentation specially.

-   Speech: If speech is selected, when the amount of indentation
    changes, NVDA will say something like \"twelve space\" or \"four
    tab.\"

-   Tones: If Tones is selected, when the amount of indentation changes,
    tones indicate the amount of change in indent. The tone will
    increase in pitch every space, and for a tab, it will increase in
    pitch the equivalent of 4 spaces.

-   Both Speech and Tones: This option reads indentation using both of
    the above methods.

If you tick the \"Ignore blank lines for line indentation reporting\"
checkbox, then indentation changes won\'t be reported for blank lines.
This may be useful when reading a document where blank lines are used to
separate indented blocks of text, such as in programming source code,
like that in our Python course.

## Installing JAWS for Windows Scripts and Configuration Setting Files

Note: We officially do not support these configuration settings or files
but provide them to you for your convenience. We will try to support
them to the best of our ability but it is only on a limited and best
effort basis.

The following steps are used to install the scripts and configuration
files for VSCode. Installing these will have these expected outcomes:

> The Read Status Bar command (JAWS Key + Page Down) will tell you the
> row and column you are at within the editor. You must make sure the
> VSCode window is maximized and that the status bar is turned on for
> this script to work. If you enable Zen Mode then the status bar will
> be turned off and this script will not function.

-   Pressing F6 now reliably tells you that you are on the status bar.

> Obtain the needed files and instructions to install the scripts from
> the [Doug Lee Visual Studio Code web
> site](http://www.dlee.org/vscode).

### Setting Up Announcements of Indentation for VSCode and JAWS

#### Checking to See if Indentation is Working in JAWS

> You may already have this working. You can tell by doing something
> like:

1.  Open VSCode and open a new file with Control + N.

2.  Write anything in the first line of the file and do the same in the
    second line of the file.

3.  Move back to the first line and move to the beginning of the line.

4.  Press the Tab key.

5.  Now move down to the second line and back for the first line.

6.  If you heard "One Tab" then indentation announcements are working
    and you need not proceed further in this section. You can also try
    deleting a space from the beginning of the line and try moving down
    and back to the first line. You should hear three spaces at this
    point. Again, if it is doing this you are all set.

#### Setting Up Indentation in JAWS

> Follow these steps to configure two settings to implement indentation
> announce in JAWS:

1.  Open VSCode. You need not have any documents open.

2.  Open the JAWS Settings Center by using the hotkey JAWS Key + 6.

3.  In the search field type "indent" and press the down arrow key. You
    should hear something like "Say Indented Characters". It is probably
    not checked. Check this by pressing the space bar.

4.  Tab to the OK button and press the Enter key.

5.  Re-open the Settings Center and tab to the tree view and move to the
    item that is entitled "Speech And Sounds Schemes".

6.  Once highlighted, press the right arrow key and then press the down
    arrow key.

7.  Now you need to define the active Sound Scheme. Press the space bar
    until you reach the Sound Scheme with the name "Indent (Tab is Four
    Spaces)". You should hear something like this once this has been
    reached "Active Speech and Sounds Scheme Indent (Tab is Four
    Spaces)".

8.  Once selected, use the Tab key and navigate to the OK button.

9.  Press the Enter key to invoke the OK button.

10. While not required, I would suggest closing and re-opening VSCode
    and testing these changes as noted in the prior section to ensure
    that the Editor and JAWS are behaving as expected.

## How to Reset VSCode Settings

You may have previously installed VSCode on your system. If so, we would
encourage you to reset your VSCode settings to their system defaults.
Close VSCode on your device before proceeding. Follow these steps to
accomplish this task:

### Completely Removing Visual Studio Code from Windows Devices

The steps outlined below, after this section, pertain to simply removing
your user settings. Extensions and other things may not be reset as a
part of this process. If you wish to complete remove VSCode and
re-install it so that Windows sees the editor from a fully fresh start
then you should follow these steps:

Note: Be warned. This requires removing files from sensitive places on
your device. Please take special caution when performing these steps.

1.  Remove Visual Studio Code from your machine by using the Installed
    Apps feature which accessible as the first option from the Windows +
    X hotkey. This is found by looking for Microsoft Visual Studio Code
    in the list of installed applications.

> Note: Each step outlined below will make use of the Windows Run
> (Windows Key + R) command. We mention this here so as not to repeat
> ourselves in the next few steps.

2.  Move to this folder on your device from the Run dialog:

> %UserProfile%\\

3.  Now remove this folder from your device if present:

> .vscode

4.  Now browse to this folder from the Run dialog:

> %AppData%\\

5.  If present, remove this folder from your device:

> Code

6.  Finally, browse to this folder:

> %LocalAppData%\\Programs\\

7.  This folder may or may not be present, but if it is remove it:

> Microsoft VS Code

8.  Re-install Visual Studio Code and launch it. You should now have a
    fully reset VSCode on your system as though it were never installed
    on your device.

> Note: The next sections simply document the removal of your user
> settings folders in VSCode. If you took the approach on your Windows
> device outlined above you need not perform these steps shown below.

### Delete Your User Settings Folder

#### Windows Devices

1.  Hold down the Windows key and press the R key to bring up the run
    dialog.

2.  Type %APPDATA%\\Code and press enter.

3.  Look for a folder called "User". Once found, simply delete the
    "User" folder.

#### MacOS Devices

1.  Open the Terminal application.

2.  Enter the following command and press Enter:

rm -rf \$HOME/Library/Application\\ Support/Code/User

### Restarting VSCode

After deleting the user settings folder, restart the VS Code
application. You should now be reset to your factory defaults.

## Getting Started with Visual Studio Code

When you launch VSCode for the first time, the editor may detect that
you are using a screen reader, such as NVDA or JAWS. If so, it will
suggest enabling the screen reader mode. This mode enhances the
editor\'s accessibility for users of screen readers. The screen reader
mode can be toggled at any time. To do so on Windows, press Alt +
`Shift + F1`. For Mac users, the shortcut is Option + `Shift + + F1`.
This will manually switch the screen reader mode on or off, depending on
your needs.

### The VSCode Welcome Screen

When you first start VSCode, a welcome screen appears. The Start group
on the left is where your focus lands. It contains shortcuts for opening
files and one to clone a Git repository. (Git is considered to stand for
Global Information tracker and is a standard method for easily sharing
code between developers. It keeps a record of all changes made allowing
groups to easily collaborate including retrieving previous versions of a
project.) A repository contains anything a developer wishes to stash
there and cloning is the act of making a local copy for yourself.

You can tab through these shortcuts to get to the next group, Recents,
which will have any recently opened files. Tabbing again takes you
through the Walkthroughs group which has product documentation,
tutorials, cheat sheets, introductory videos, and access to other
training materials and learning resources about VSCode. What appears
here will be different, depending on whether you\'ve already installed
language extensions. You can investigate any of these now, or keep
tabbing.

At last you get to a checkbox labeled \"When checked, this page will be
shown on startup\". Uncheck it if you find the welcome screen annoying
or keep it checked if you like it. Unchecking it means you won\'t have
that welcome screen automatically appearing again. But you can get it
back by selecting \"Welcome\" under \"help\".

If you keep the welcome screen, you\'ll need to press F6 to move to the
main workspace, which will be explained below in detail. If you uncheck
it, you\'ll hear the message \"Saving\" and be dropped directly in to
the main workspace.

### Starting VSCode in your BITS Folder and Trusting the Folder

Let's all go into Terminal and launch VSCode from your BITS folder. Once
you have launched the terminal make sure to move to the location of your
BITS Folder. Once here type:

code .

Meaning, type "code" followed by a space and then the period punctuation
symbol. This will launch VSCode in your BITS folder. If this is the
first time you have launched VSCode for this folder you will be prompted
to trust the folder. Answer Yes to this prompt. This will ensure that
future confirugations will work correctly, especially when configuring
your Python Interpreter.

## Navigating the VSCode Interface with a Keyboard

There are two primary methods for navigating the VSCode user interface
using a keyboard: the Tab key and the F6 key.

### Using the Tab Key

The Tab key serves a dual purpose in VSCode:

1.  Indenting code: In programming languages like Python, correct
    indentation is crucial. The Tab key can be used to create these
    indents.

2.  Navigating UI elements: The Tab key can also move focus to the next
    interactive element within VSCode.

Users can switch between these two functions by pressing `Ctrl + M` on
Windows or `Cmd`` + M` on a Mac. When set to navigate between elements,
the Tab key operates as expected in most Windows applications. For
instance, if the focus is in the main editor area (which might be
identified as a \"main landmark region\" by screen readers, depending on
verbosity settings), pressing Tab will move focus to the status bar or
the next open pane in the tab sequence. Conversely, pressing Shift + Tab
usually navigates to the breadcrumb trail, which displays the path to
the currently open file.

### Using the F6 Key

Pressing the F6 key allows the user to move the cursor between different
sections of the editor, such as the main editor area, the status bar, or
the activity bar.

By combining these two keys, users can efficiently navigate and interact
with the various components of the VSCode interface.

## The Main Workspace

There are quite a few items to know about in this workspace. The
largest, and where you will spend most of your time is the editor. But
various panes and panels are also available to let you open files,
locate folders, locate text within files, access repositories and debug
your code.

### The VSCode Editor

You can have multiple editor windows open, but most visually impaired
learners will not want that confusion at first. If you do open multiple
editor windows, by default, they will appear at the right of the first
opened window and you can use Control with the number keys to jump
between them. For example holding control and pressing the number 3 on
your standard keyboard will open the third editor window.

To open an existing file, press CTRL-O or Command-O on the Mac. To
create a new file, press CTRL-N or Command-N on the Mac. You\'ll now
have an editor within which you can work. Note, that unlike Microsoft
Word, a blank document will not automatically open.

If you need to close anything either in the interface or in the editor,
press CTRL+SHFT+W.

If you need to make things bigger, you can press Control along with the
plus key to zoom up, and control with the minus key to zoom down. This
will zoom the entire interface, not just the editor.

As a reminder, you type in this editor as you would in any word
processor. If you press the tab key an indent is inserted, unless you
toggle this behavior with CTRL+M for Windows users and CTRL+Shift+M for
Mac users, in which case, a tab character will be inserted. In other
areas of the interface, pressing tab will navigate between elements.

Note: If you are using NVDA you may want to consider the use of
third-party addons to assist with indent navigation hotkeys by
installing this [NVDA
addon](https://marketplace.visualstudio.com/items?itemName=TonyMalykh.indent-nav).

The usual cut, copy and paste keyboard shortcuts work, as well as
highlighting (selecting) text with the mouse or the shift and arrow
keys. However, you can use anchors to select text as well. Begin your
selection with \`CTRL+KB\` and end it with \`CTRL+KD\`. This marks a
section for you to act on it, such as cutting, copying or performing
more advanced functions. If you are old enough to remember Wordstar,
this behavior of selecting blocks is identical.

A handy command to delete the current line is \`Ctrl + Shift + K\`. To
go to a particular line by entering its number, press Ctrl + G.

There are hundreds of keyboard shortcut hotkeys (called key bindings)
and you can see all or alter any of them by pressing \`CTRL+K+CTRL+S\`.

### The VSCode Menu Bar

The Menu Bar is a horizontal bar located at the top of the window, with
hierarchical drop-down menus to provide the user with a place to find
most of the essential functions in VS Code. The fastest way to access
the Menu Bar is to press \`ALT\`. Then use the left and right arrow keys
to navigate the top-level menu: \`File \| Edit \| Selection \| View \|
Go \| Run \| Terminal \| Help\` or you can use the first letter
navigation. For example: press ALT then the letter T to jump straight to
the terminal menu. Use the up and down arrow keys to navigate the
hierarchical drop-down menus. Press Escape to leave the menus.

### The VSCode Status Bar

Below the editor, the status bar appears. It has some quick actions
shortcuts and information about the file currently being edited. This
includes the line and column number of the cursor, the language that
VSCode thinks you are using, the line terminator (Windows, Mac or Linux)
and the tab size, which defaults to four spaces, but can easily be
changed. There are also several other pieces of information. The status
bar also contains the errors and warnings detected, whether you\'re
remotely connected, plus notifications. As a beginner, it\'s not
necessary to understand all the information displayed here. One
important message is: \"screen reader optimization is enabled\". This
should appear; if it does not, use the keystroke Shift + Alt + F1 to
toggle it.

Use the \`spacebar\` to activate a status bar item, for example to
change the language or the number of spaces in a tab stop. You can move
through these status indicators with the left and right arrow keys, but
you must press F6 several times to cycle back to the editor. (If you are
low-vision you will notice the lefthand side of the status bar contains
the shortcuts for collaboration while the righthand portion contains
details about the current file.)

### The VSCode Activity Bar

The Activity Bar in Visual Studio Code is a vertical toolbar located on
the far left-hand side of the window, facilitating quick access to
different views and features. It features icons for the File Explorer,
Search, Source Control, Debug, and Extensions. Keyboard users can
navigate to the Activity Bar by pressing F6.

For screen reader users, the Activity Bar is referred to as the \"Active
View Switcher\" and is presented as a list of vertical tabs. Navigation
through this list is accomplished with the up or down arrow keys,
allowing the cursor to move between panels. The screen reader announces
the name of each panel along with its status (expanded or collapsed) and
the corresponding keyboard shortcut. These shortcuts enable toggling of
the respective panel from anywhere within the editor. For instance,
pressing Ctrl+Shift+E on Windows, or Cmd+Shift+E on Mac, moves the
cursor to the integrated file explorer, with a second press returning
focus to the editor area. This feature facilitates efficient navigation
between the editor and various panels.

Multiple panels can be open simultaneously, which may not pose an issue
for users relying solely on a screen reader and keyboard but could
present challenges for visual users or blind users attempting to share
their screen. To collapse all panels in the Activity Bar and move focus
to the editor area (if it was not already there), one can press Ctrl+B
on Windows or Cmd+B on Mac.

There are five available sidebars:

**- Explorer**: This panel displays files, folders, and open editors
within your workspace, offering a structured view of your project\'s
directory. To focus on it, use `Ctrl+Shift+E` (Windows) or `Cmd+Shift+E`
(Mac).

**- Search**: Offers project-wide text search capabilities, including
filtering and replacement options, to help you quickly find and modify
code. Access it with `Ctrl+Shift+F` (Windows) or `Cmd+Shift+F` (Mac).

**- Source Control**: Facilitates version control management by showing
changes, staging, commits, and interactions with remote repositories.
This panel can be accessed with `Ctrl+Shift+G` (Windows) or
`Cmd+Shift+G` (Mac).

**- Extensions**: Allows you to browse, install, update, and manage
VSCode extensions, enhancing the editor with additional functionalities.
Focus on this panel with `Ctrl+Shift+X` (Windows) or `Cmd+Shift+X`
(Mac).

**- Problems Pane**: Consolidates errors, warnings, and informational
messages identified in the active file, streamlining the process of code
verification and optimization. Access and navigate within this panel by
pressing `Ctrl+Shift+M` (Windows) or `Cmd+Shift+M` (Mac). Press `Enter`
on a message to move focus to the associated line of code in the editor.

The Activity bar also has these buttons:

\- Accounts button: Lets you synchronize settings with a Microsoft or
github account across multiple machines.

\- Settings Button: \`(Ctrl +, (Comma))\` Lets you work through multiple
preferences groups to adjust this highly configurable application to
your needs.

Note that your screen reader identifies these buttons as part of a
toolbar.

### The VSCode Command Palette 

The command palette is an integral element in Visual Studio Code
(VSCode) that becomes indispensable once you get accustomed to using it.
It allows for searching and execution of any VSCode command by its
description or the associated keyboard shortcut (key binding).

To open the command palette you can press `Ctrl + Shift + P` on Windows
or `Cmd`` + Shift + P` on a Mac. Focus will land in a text field where
you can type the name of the command you are looking for or the
associated keyboard shortcut. Your most frequently used commands will
appear first in the list over time. The screen reader will announce the
number of items that match your search as well as the first element
highlighted in the list. You can navigate the filtered list with the up
or down arrow keys and the screen reader will announce each command
along with its corresponding key binding, if one is defined, such as
\"Delete Line, Control+Shift+K\".

By pressing Enter on a selected command it will be executed.

Pressing the Tab key moves focus to a toolbar with an option to
configure the key binding for the selected command. To close the command
palette, press the Escape key.

### The VSCode Panels Area

Below the editor, messages that VSCode needs to display appear in the
panels area, and in most cases are read out loud by a screen reader.
There are four panels: Problems \`(Ctrl+Shift+M)\`, Output
\`(Ctrl+Shift+U)\`, Debug Console \`(CTRL+SHIFT+Y)\` and Terminal\`
(CTRL+')\`. By default they become visible only when they have messages
to display, but you can force them to display with the keystrokes given
or press CTRL+J to make them disappear.

It is important for low-vision users to know that nearly all of these
interface elements can be moved and resized using the mouse in the usual
way. There are plenty of videos on the internet to demonstrate this.
This will have no effect on the screen reader\'s ability to read items
that are in focus or items which need to be announced automatically,
such as an error or a IntelliSense choice.

#### Using Zen Mode

A keystroke especially useful for a vision-impaired user is \`Ctrl+KZ\`
which enables \"Zen mode\" making everything but the editor invisible,
that is, putting the editor in to a full-screen mode. Press Escape twice
to exit Zen Mode. Zen mode can also be customized under Settings.

Note: If you want VSCode to start with Zen Mode enabled by default then
install this extension "zen-vscode.zen-mode-on-startup". Make sure to
read the readme after the extension is installed to understand how this
extension operates. There are situations where it will not enable Zen
Mode by default.

## Accessibility Help in Visual Studio Code

Accessibility Help in VSCode is a feature that offers comprehensive
details about the currently focused editor section. It also provides a
list of pertinent keyboard shortcuts. Windows users can access this
feature by pressing `Alt + F1`, and Mac users by pressing `Option + F1`.
When triggered, it will open a text editor containing valuable
information tailored to the segment of the editor in focus. This
includes a variety of keyboard commands and recommended actions.

While in the Accessibility Help window, pressing `Shift + Tab` will move
the focus to a toolbar. This toolbar consists of buttons designed to
facilitate interaction with the Accessibility Help feature, such as the
option to disable the hint message that instructs how to call upon the
Accessibility Help where it is available. Additionally, you can close
the Accessibility Help by pressing the `Escape` key. Familiarizing
yourself with this section early on can be greatly beneficial as you
become accustomed to the editor.

## The Accessible View in Visual Studio Code

The Accessible View in Visual Studio Code is specifically tailored to
help users of screen readers interact with content that is typically
announced by the screen reader but might not be navigable using the
keyboard alone. This functionality is incredibly useful in scenarios
where one would normally rely on screen reader review features, such as
NVDA\'s Object Navigator or VoiceOver\'s cursor, to read certain types
of content. Examples include the tooltips mentioned earlier, inline
completion suggestions, VSCode notifications, or responses in the
Copilot chat.

The Accessible View renders content in a text editor format that allows
for navigation using the arrow keys. This is somewhat akin to the
accessibility help feature we discussed previously. While examining
content in the Accessible View, users can press Shift+Tab to reach a
toolbar that offers buttons for interacting with the present content.
For example, when reviewing a code suggestion from inline completion,
there are buttons provided to accept the suggestion or to turn off the
accessibility hint that notifies users of the availability of the
Accessible View for that particular instance.

To open the Accessible View, Windows users can press Alt+F2, while Mac
users can press Option+F2. When encountering content that is announced
by the screen reader but not navigable with the keyboard, pressing this
key combination can reveal whether the Accessible View is an option.
Generally, the availability of the Accessible View is announced by
default through a hint, which users have the option to disable in the
settings if desired.

## Accessibility signals

Accessibility signals encompass both sounds, formerly called audio cues,
and announcements, formerly called alerts. Accessibility Signals may
indicate if the current line has certain markers such as: errors,
warnings, breakpoints, folded text regions or inline suggestions. They
are played when the primary cursor changes its line or the first time a
marker is added to the current line. The commands Help: List Signal
Sounds and Help: List Signal Announcements allow users to view the
available signals and configure them. Migration to this new
configuration happens automatically.

## Interacting with Hover Content in Visual Studio Code

Visual Studio Code provides information by hovering the mouse over
certain content. For instance, if you hover the mouse over a function,
it will display information about the arguments that the function
accepts. While debugging, if you hover over a variable, it will show the
value of that variable as a tooltip. To trigger these tooltips and have
them read by a screen reader, first place the cursor on the text you
suspect will activate the tooltip. On Windows, press Ctrl+K and then
Ctrl+I; on a Mac, use Cmd+K followed by Cmd+I. The tooltip will appear
visually and be read aloud by the screen reader. While the tooltip is
visible, you can also read it using the accessible View.

### Disabling Tooltips in Visual Studio Code

Tooltips in Visual Studio Code can be disruptive for some users,
especially for those with low vision. If necessary, they can be turned
off. To do this, access Settings by pressing Ctrl+, on Windows or Cmd+,
on a Mac. The Settings window will open in a new tab with the keyboard
focus on the search field. Enter \"hover\" in the search box. This will
bring up various settings related to hover functionality. Look for the
setting titled \"Editor: Hover Enabled.\" Navigate through the results
using the down arrow key. When you reach the \"Editor: Hover Enabled\"
setting, press the Tab key to move the focus to the associated checkbox,
and toggle it off using the Spacebar. Once you finish adjusting the
settings, close the tab by pressing Ctrl+W on Windows or Cmd+W on a Mac.

## Interacting with Notifications in Visual Studio Code

In Visual Studio Code (VSCode), various notifications inform users about
events taking place within the editor. These notifications might be
purely informational or require user action. For instance, when typing
text in a new file, if VSCode recognizes the content as Python code, it
may present a notification indicating that Python has been detected and
suggest installing the Python extension if it\'s not already installed.
This is a scenario where you might want to interact with the
notification to install the recommended extension.

To engage with a notification, you can use the Accessible View feature
previously discussed. To accept a notification\'s prompt, on Windows,
you can press Ctrl+Shift+A, or Cmd+Shift+A on a Mac.

You can also browse through all notifications using the keyboard. To do
so, cycle through the editor\'s elements by pressing F6 until the screen
reader announces that focus is in the status bar. Next, navigate through
the icons in the status bar using the left and right arrow keys until
you find the notifications icon and press Enter. This action opens the
Notification Center, which can be navigated using the up and down arrow
keys. To interact with a specific notification, use the Tab key to move
through the available actions. To exit the Notification Center and
return to the editor, simply press the Escape key.

Additionally, it\'s possible to open the Notification Center directly by
pressing Ctrl+K followed by Ctrl+Shift+N on Windows, or Cmd+K followed
by Cmd+Shift+N on a Mac.

## Additional Keyboard Shortcuts

VSCode incorporates numerous keyboard shortcuts to facilitate access to
its various features and tools. The subsequent list is not comprehensive
but serves as a primer to utilizing the editor. Additionally,
customization of keyboard shortcuts is possible through the settings
menu. Be aware that certain commands can vary depending on your
operating system, Windows or Mac.

-   **Quick File Search**: Conduct a quick search for files using
    `Ctrl+F` (Windows) or `Cmd+F` (Mac). Use `Enter` to navigate to the
    next occurrence or `Shift+Enter` for the previous. The screen reader
    will announce the line and occurrence index. Press `Escape` to exit
    the search dialog.

-   **Symbol Navigation**: Navigate to specific symbols or definitions,
    such as variables or functions, by pressing `Ctrl+Shift+O` (Windows)
    or `Cmd+Shift+O` (Mac) and typing the symbol\'s name.

-   **Symbol Renaming**: To rename symbols and update all references
    throughout the code, press `F2`.

-   **Line Navigation**: To hear the current line number or move to a
    different line of code by its number, press `Ctrl+G` on Windows and
    Mac.

-   **Navigate to Next/Previous Line with a Problem**: Use `F8` to
    navigate to the next line with a problem, and `Shift+F8` to navigate
    to the previous line with a problem.

-   **Open External Terminal**: To open an external terminal in the
    folder of the active workspace, press CTRL`+Shift+C` on Windows, or
    Cmd`+Shift+C` on Mac.

## Configuring Useful Settings in VSCode

> VSCode offers a vast number of settings to control the look, feel and
> behavior of the editor. We will point out a few of these settings that
> you might want to consider changing for optimal use with a screen
> reader.

### Installing the Python Extension

> Follow these steps:

1.  Open VSCode and press CTRL+Shift+X to install an extension.

2.  Search for Python and highlight this specific extension:

> Python, 2024.2.1, Verified Publisher Microsoft, Python language
> support with extension access points for IntelliSense (Pylance),
> Debugging (Python Debugger), linting, formatting, refactoring, unit
> tests, and more. 
>
> Note: The version number may be different from shown above.

3.  Tab to the Install button and press the space bar to activate it.

### Configuring the Python Interpreter

> Follow these steps:

1.  Open VSCode.

2.  Press CTRL+Shift+P to open the command Palette.

3.  Type Python and select the option that states:

> Python: Select Interpreter
>
> and press the Enter key.

4.  Now, select the version of Python you have installed. On the machine
    that this document is being prepared on the version number is:

5.  

> Python 3.12.1 64-bit
>
> Anything close to this version number is more than sufficient.

### Opening and Using VSCode Settings

> To open Settings in VSCode, press CTRL + comma in Windows and Cmd plus
> comma on the Mac. Once in this dialog you can type keywords to modify
> specific settings.

#### Silencing inline and IntelliSense Announcements by the Screen Reader

> Students may wish to deactivate IntelliSense. IntelliSense is a
> feature that provides automatic suggestions and information about the
> code
>
> as you type. Once disabled, it can be triggered manually with CTRL
> +Space. This is very much an individual choice so you may want to
> leave things at the default to see if you prefer this before changing
> this behavior. Follow these steps to make these changes:

1.  Open Preferences from the File Menu and select Settings, or use CTRL
    plus Comma on Windows or CMD plus Comma on the Mac.

2.  Type "QuickSuggest" and arrow down to the option "Editor Quick
    Suggestions" and press the enter key. Three options will be shown
    here.

3.  You should hear something like the following:

> The property \`other\` is set to \`on\`.

6.  Tab twice to the Edit button and press the space bar.

7.  Expand the combo box with Alt plus down arrow and move to the off
    selection and press Enter.

8.  Press the Escape key twice to go back to the Search field and clear
    out the field.

9.  Type "Trigger" and press down arrow until you hear "Editor Suggest
    On Trigger Characters. Controls whether suggestions should
    automatically show up when typing trigger characters.".

10. Press Enter and uncheck the checkbox that is shown.

#### Configuring the External Terminal for Windows Users

Configuring the external terminal for windows users is about telling vs
code what to launch on the ctrl+shift+c keyboard shortcut (assuming you
haven't changed any keyboard shortcuts).  The default is to launch
cmd.exe. Follow these steps:

1.  Open the Terminal and issue this command:

> Where.exe pwsh.exe \| clip.exe

Note: This assumes you are configuring your external terminal to use
PowerShell 7.

Doing this command puts the full path to PowerShell 7's executable on
your clipboard, which we will use later.

If you want to use the terminal app, that command is wt.exe:

> Where.exe wt.exe \| clip.exe
>
> This will copy Terminal's complete path and filename to the clipboard
> which you can also use further in the documentation.

2.  Open Settings in VSCode and search for
    "terminal.external.windowsExec".

3.  Press the down arrow key to highlight the item just searched for.

4.  Tab to the edit field where you most likely will see a full path
    with cmd.exe being executed at the end of the string.

5.  Replace this text by pasting what you just copied on to the
    clipboard.

## Final Remarks

In this document, we\'ve aimed to highlight key aspects of using VSCode
with a screen reader and keyboard. We\'ve also included features
beneficial to low vision users, such as the ability to disable tooltips
or visually collapse all panels in the status bar. Our objective is to
provide a comprehensive guide to help users get started with the editor
in a user-friendly manner. However, this does not replace VSCode\'s
official documentation. For more in-depth information about the features
discussed here and beyond, we strongly recommend spending time reviewing
the accessibility page for VSCode, available at [VSCode
Accessibility](https://code.visualstudio.com/docs/editor/accessibility).

## History of Changes

### August 4, 2024

- Added instructions to configure line indentation reporting for VoiceOver on macOS 

### March 19, 2024

-   Added documentation on configuring indentation settings for NVDA
    users.

### March 17, 2024

-   Added documentation on installing your Python Extension for VSCode.

-   Added documentation on defining your Python Interpreter.

-   Added better steps to revise your external Terminal setting for
    VSCode.

-   Added language to start VSCode in your BITS folder and trusting your
    folder once VSCode has launched. This is vital for configuration
    steps later.

### March 11, 2024

\- Added language pertaining to [addons for
NVDA](https://marketplace.visualstudio.com/items?itemName=TonyMalykh.indent-nav)
to assist with indentation navigation.

\- Corrected the keystroke for the Mac for the VSCode Go to command from
CMD to CTRL.

\- Revised the instructions for installing the VSCode JAWS scripts.

Added sections on implementing indentation announcements for JAWS users
with the Visual Studio Code editor.
