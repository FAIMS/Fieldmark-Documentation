# User Roles

In this Guide we explain the different types of user accounts and their roles in Fieldmark.

Users can be granted permission to see and edit Notebooks, individual records in notebooks and Workspaces depending on the way their account has been registered by the Administrator. It is important to be aware of your login details when using Fieldmark.  

## User Roles in Fieldmark



### Users
:::{index} user-role; user
:::


The default type of Fieldmark user (Role=User). They can:

- see and activate any Notebooks that have been made available to them by an administrator
- create and edit their own records in those Notebooks
- create local Notebooks but not share them with other users  

A User cannot:

- see or edit the records of other Users
- see Notebooks unless granted permission by an administrator

### Administrators
:::{index} user-role; administrator
:::

There are two types of administrators:

- Notebook Administrators (Role=Admin)
- Workspace Administrators (Role=ClusterAdmin)

Notebook Administrators (Admins) can:

- do everything a User can,
- see and edit records created by other users, and
- give permission for other Users to access a Notebook.  

Workspace Administrators (ClusterAdmins) can:

- do everything that a Notebook Administrator can
- give permission for other Admins to manage a Notebook
- see all Notebooks on the Workspace
- create and edit Notebooks to be shared with other Users in their Team or Enterprise.

For instructions of how to manage user groups go to [User Management](user-management).

## How to check your Account credentials

If you are unsure which account you have logged in as, check the name which appears in to the right hand corner of the screen: {% include figure image_path="//images/accountlogin.jpg" alt="account login" %}

To identify the role you have been assigned, choose 'User' from the Navigation Sidebar. Your role: {% include figure image_path="//images/userscreen.jpg" alt="user screen"%}  

## Switching Users

If you are sharing devices with colleagues on the same field campaign, you may wish to stay logged in to different accounts and switching between them for different tasks. To do this:

1. Choose 'Switch User' from the top right hand corner of the menu Sidebar
2. Choose an Active User from the dropdown list and select 'Switch'
3. Or, select the 'Add Another User' button to sign in another user

### Adding Other users

To add another **Google** account, follow the link at the bottom of the User screen.

If you are signed in with **Data Central** and wish to add another Data Central user you need to sign out using the [DC logout]( https://auth.datacentral.org.au/cas/logout) first (as Data Central only allows for one signed-in user at a time). Once you have signed in with a different user you can switch between both users.
