# Test automation project for [Petstore](https://petstore.swagger.io/)

# <a name="TableOfContents">Table of contents</a>
+ [Description](#Description)
+ [Tools and technologies](#Technology)
+ [How to run](#HowToRun)
    + [Run in Jenkins](#RunInJenkins)
+ [Telegram Notifications](#TelegramNotifications)
+ [Test results report in Allure Report](#AllureReport)
+ [Allure TestOps integration](#AllureTestOps)
+ [Jira integration](#Jira)


# <a name="Description">Description</a>
The test project consists of API tests.

[Back to the table of contents ⬆](#TableOfContents)

# <a name="Technology">Tools and a technologies</a>
<p  align="center">
  <img src="resources/images/logo/python.svg" width="5%" alt="Python"/>
  <img src="resources/images/logo/pytest.png" width="5%" alt="Pytest"/>
  <img src="resources/images/logo/pycharm.png" width="5%" alt="PyCharm"/>
  <img src="resources/images/logo/jenkins.png" width="5%" alt="Jenkins"/>
  <img src="resources/images/logo/Allure.svg" width="5%"  alt="Allure"/>
  <img src="resources/images/logo/Allure_TO.svg" width="5%" alt="Allure TestOps"/>
  <img src="resources/images/logo/telegram.svg"width="5%" alt="Telegram"/>
</p>

The autotests in this project are written in `Python` using `Pytest` framework.\
`Jenkins` - CI/CD for running tests remotely.\
`Allure Report` - for test results visualisation.\
`Telegram Bot` - for test results notifications.\
`Allure TestOps` - as Test Management System.

[Back to the table of contents ⬆](#TableOfContents)

# <a name="HowToRun">How to run</a>

To run locally and in Jenkins the following command is used:
```bash
pytest .
```

[Back to the table of contents ⬆](#TableOfContents)


## <a name="RunInJenkins">Run in [Jenkins](https://jenkins.autotests.cloud/job/C01-miserylab-petstore-api-test-project/)</a>
Main page of the build:
<p  align="center">
  <img src="resources/images/jenkins1.png" alt="JenkinsBuild"/>
</p>


After the build is done the test results are available in:
>- <code><strong>*Allure Report*</strong></code>
>- <code><strong>*Allure TestOps*</strong></code>

<p  align="center">
  <img src="resources/images/jenkins2.png" alt="JenkinsFinishedBuild"/>
</p>

[Back to the table of contents ⬆](#TableOfContents)


# <a name="TelegramNotifications">Telegram Notifications</a>
Telegram bot sends a brief report to a specified telegram chat by results of each build.
<p  align="center">
<img src="resources/images/telegram.png" alt="TelegramNotification" >
</p>

[Back to the table of contents ⬆](#TableOfContents)

# <a name="AllureReport">Test results report in [Allure Report](https://jenkins.autotests.cloud/job/C01-miserylab-petstore-api-test-project/28/allure/)</a>


<p align="center">
  <img src="resources/images/allure1.png" alt="AllureReport1">
</p>

<p align="center">
  <img src="resources/images/allure2.png" alt="AllureReport2">
</p>


[Back to the table of contents ⬆](#TableOfContents)

# <a name="AllureTestOps">[Allure TestOps](https://allure.autotests.cloud/project/1655/dashboards) integration</a>
> The link can be accessed only by authorized users.

## <a name="AllureTestOpsProject">Project in Allure TestOps</a>


<p align="center">
  <img src="resources/images/testops1.png" alt="Allure Report"/>
</p>

<p align="center">
  <img src="resources/images/testops2.png" alt="Allure Report"/>
</p>

<p align="center">
  <img src="resources/images/testops3.png" alt="Allure Report"/>
</p>


[Back to the table of contents ⬆](#TableOfContents)

# <a name="Jira">[Jira](https://jira.autotests.cloud/browse/HOMEWORK-422) integration</a>
> The link can be accessed only by authorized users.
<p align="center">
  <img src="resources/images/jira.png" alt="Jira integration"/>
</p>

[Back to the table of contents ⬆](#TableOfContents)


