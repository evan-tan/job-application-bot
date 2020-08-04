from pathlib import Path

home = str(Path.home())

PROFILE = {"chrome": home + "/.config/google-chrome",
           "firefox": ""}

WEBDRIVER_PATH = {"chrome": home + "/bin/chromedriver",
                  "firefox": ""}

PORTAL = {"glassdoor": "https://www.glassdoor.com.au/index.htm",
          "linkedin": "https://www.linkedin.com/jobs",
          "careergateway": "https://careergateway.monash.edu.au"
          }