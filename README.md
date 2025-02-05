<img src="https://raw.githubusercontent.com/euroargodev/argopy/master/docs/_static/argopy_logo_long.png" alt="argopy logo" width="200"/> 


# Argopy online resource status

[![Erddap](https://img.shields.io/endpoint?label=src%3D%27erddap%27&style=for-the-badge&url=https://raw.githubusercontent.com/euroargodev/argopy-status/master/argopy_api_status_erddap.json)](https://argopy.statuspage.io/)

[![Argovis status](https://img.shields.io/endpoint?label=src%3D%27argovis%27&style=for-the-badge&url=https://raw.githubusercontent.com/euroargodev/argopy-status/master/argopy_api_status_argovis.json)](https://argopy.statuspage.io/)

[![GDAC](https://img.shields.io/endpoint?label=src%3D%27gdac%27&style=for-the-badge&url=https://raw.githubusercontent.com/euroargodev/argopy-status/master/argopy_api_status_gdac.json)](https://argopy.statuspage.io/)

Check is performed approximately every 5 mins and results stored in json files on this repo.

Date of files above reflect the time since API status did not changed.

**You can also check and subscribe to monitoring results at https://argopy.statuspage.io**

Other possible monitoring page: https://stats.uptimerobot.com/n8zoRtGnwl

Markdown to insert default badges:

    ![Erddap status](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/euroargodev/argopy-status/master/argopy_api_status_erddap.json)
    
    ![Argovis status](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/euroargodev/argopy-status/master/argopy_api_status_argovis.json)

    ![GDAC status](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/euroargodev/argopy-status/master/argopy_api_status_gdac.json)

# Energy impact 

## Continuous Integration tests of argopy

Since the last argopy release, the execution of unit tests on Github Actions for all merged PRs so far is evaluated as:

![CarbonFootprint](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/euroargodev/argopy-status/master/argopy_carbonfootprint_since_last_release.json)


## API status monitoring

[![CI Energy][ci-energy-badge]][ci-energy-link]

<a href="https://metrics.green-coding.io/ci.html?repo=euroargodev/argopy-status&branch=master&workflow=2724029"><img src="https://api.green-coding.io/v1/ci/badge/get?repo=euroargodev/argopy-status&amp;branch=master&amp;workflow=2724029&amp;mode=totals&amp;metric=carbon&amp;duration_days=30"></a>

[More details on the Green-coding page here][ci-energy-link]

[ci-energy-badge]: https://api.green-coding.io/v1/ci/badge/get?repo=euroargodev/argopy-status&branch=master&workflow=2724029&metric=carbon
[ci-energy-badge-30]: https://api.green-coding.io/v1/ci/badge/get?repo=euroargodev/argopy-status&branch=master&workflow=2724029&metric=carbon&mode=total&duration_days=30
[ci-energy-link]: https://metrics.green-coding.io/ci.html?repo=euroargodev/argopy-status&branch=master&workflow=2724029
