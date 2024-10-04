# UBC Rogers CAMARA Hackathon

- [UBC Rogers CAMARA Hackathon](#ubc-rogers-camara-hackathon)
- [CAMARA Project](#camara-project)
  - [Rogers CAMARA APIs](#rogers-camara-apis)
  - [Roger's Sample Test Cases](#rogers-sample-test-cases)
  - [Subscriber Consent](#subscriber-consent)
  - [Getting Started](#getting-started)
  - [Access Tokens](#access-tokens)
  - [Sandbox](#sandbox)
  - [In the News](#in-the-news)
  - [Quick Links/Resources](#quick-linksresources)

# CAMARA Project

CAMARA’s official documentation provides you with all information you need to get started. official github repos provides you with all updates.

* Project Home Page - https://camaraproject.org/
* Official Repositories - https://github.com/camaraproject

## Rogers CAMARA APIs

* Curent
  * NumberVerify - https://camaraproject.org/number-verification/ 
  * SIMSWAP - https://camaraproject.org/sim-swap/
  * Location - https://camaraproject.org/device-location/
* Future
  * OTP - https://camaraproject.org/number-verification-sms-2fa/
  * QoD - https://camaraproject.org/quality-on-demand/

## Roger's Sample Test Cases

* [NumberVerify](tests/test-api-location-verification.html)
* [Location](tests/test-api-location-verification.html)
* [SIMSWAP](tests/test-api-sim-swap.html)

## Subscriber Consent

Consent is a key part of the CAMARA project. The subscriber must provide consent before any of the APIs can be used. The consent process is triggered inline with the API call. The subscriber will receive a consent request via SMS. The subscriber must reply with a YES to provide consent. The subscriber can also reply with a NO to deny consent.

## Getting Started

```bash
curl -X POST "{basename}/number-verification/v0/verify" \
-H "Authorization: Bearer {your_access_token}" \
-H "Cache-Control: no-cache" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-d '{
  "phoneNumber": "+1416XXXXXXX"
}'
```

## Access Tokens

Access tokens are required to access the Rogers APIs. During the hackathon, each team will receive a test device and SIM card. The test device will contain a RAPID shortcut app that will display your access token. APIs and access tokens will be restricted to only validate the phone number associated with the SIM card provided to your team.

## Sandbox

Currently we have an Azure sandbox proxying the requests to the CAMARA APIs. The sandbox is available at https://sandbox.camaraproject.org/. The sandbox is a temporary solution and will be replaced with a Azure Programmable Connectivity (APC). This can also be used to troubleshoot any issues with the APIs. 

* [Sandbox](https://lemon-bush-0e5bf4e0f.5.azurestaticapps.net/) - https://lemon-bush-0e5bf4e0f.5.azurestaticapps.net/
* basename: https://pplx.azurewebsites.net/api/rapid/v0/

## In the News

* https://mobilesyrup.com/2023/03/01/rogers-and-microsoft-enter-new-5g-partnership/

## Quick Links/Resources

* Ecosystem Documentation (GSMA, CAMARA, TMF) - https://www.gsma.com/solutions-and-impact/technologies/networks/wp-content/uploads/2023/05/The-Ecosystem-for-Open-Gateway-NaaS-API-development.pdf

* Open API - https://www.openapis.org/

* API as a Service - https://backendless.com/what-is-api-as-a-service/

* System Design - https://github.com/donnemartin/system-design-primer
