# CRA Product Classification & Access Control Matrix — Industrial Servo Drive

- Version: 0.1
- Date: 2026-11-13
- Scope: generic industrial servo drive / drive family; CRA only
- Status: legal framework checked; product-specific classification and implementation remain UNVERIFIED pending SKU, intended purpose, system boundary and technical evidence.
- Legal baseline: Regulation (EU) 2024/2847 and Commission Implementing Regulation (EU) 2025/2392, EUR-Lex official texts.

## 1. Executive conclusion

A servo drive must not be labelled automatically as an Annex III Class I or Class II important product merely because it is network-connected, used in industrial automation, or can influence motion. The CRA classification test is based on whether the product **as a whole has the core functionality** of a category listed in Annex III, read with the technical descriptions in Implementing Regulation (EU) 2025/2392.

The Annex III Class II categories are limited to:
1. Hypervisors and container runtime systems supporting virtualised execution;
2. Firewalls, intrusion detection and prevention systems;
3. Tamper-resistant microprocessors;
4. Tamper-resistant microcontrollers.

Neither “industrial automation and control systems”, “PLC”, “motion controller” nor “servo drive” is expressly listed as a Class II category in Annex III. An embedded network interface, firewall-like feature, security chip or other component does not automatically classify the complete drive as an important product. The whole product's core functionality and the exact technical description must be assessed.

Regardless of important-product classification, a product with digital elements in CRA scope remains subject to the applicable general CRA essential cybersecurity requirements, manufacturer obligations, risk assessment, technical documentation and conformity assessment route.

## 2. Product boundary and classification decision

| Gate | Question / evidence needed | Current status | Decision rule |
|---|---|---|---|
| A. CRA scope | Does the marketed product contain software/data and allow direct or indirect logical/physical data connection to a device/network? | UNVERIFIED | Establish intended purpose, interfaces, connectivity, and whether the item is marketed as a product with digital elements. |
| B. Product boundary | Is the assessed item a standalone drive, drive + engineering software, network option module, controller, or a larger machine/system? | UNVERIFIED | Define product boundary and separate products/components placed on the market from integrated components. |
| C. Core functionality | What is the product's primary function as marketed and documented? | UNVERIFIED | Use intended purpose, datasheet, user manual, architecture and actual marketed function. |
| D. Annex III match | Does the whole product's core functionality meet one of Annex III categories and the technical description in Implementing Regulation 2025/2392? | UNVERIFIED | Do not infer a match from industrial use or an integrated component alone. |
| E. Class and route | If a category matches, is it Class I or II and which Article 32 route applies? | UNVERIFIED | Apply Article 32(1)–(3) only after category matching. |
| F. Other legislation | Does the same product also fall under other Union harmonisation legislation (e.g. machinery/electrical/EMC)? | UNVERIFIED | Coordinate the CRA assessment and technical documentation with applicable sectoral legislation; do not assume CRA replaces it. |

### 2.1 Annex III cross-check

| CRA Annex III category | Class | Generic servo drive conclusion |
|---|---|---|
| Identity management / privileged access management | I | Not established; a drive's local account system alone does not prove that its core function is identity management. |
| Physical and virtual network interfaces | I | A network interface embedded in a drive does not by itself establish that the whole drive's core functionality is a network interface. Review any separately marketed interface product/module. |
| Operating systems / boot managers / network management systems | I | Not established from the generic servo-drive description. |
| Hypervisors / container runtime systems | II | Not ordinarily the drive's core functionality; verify if the product is actually such a platform. |
| Firewalls / IDS / IPS | II | A drive with filtering or monitoring features is not automatically a firewall/IDS/IPS product; core functionality must meet the technical description. |
| Tamper-resistant microprocessors / microcontrollers | II | A security chip inside the drive does not automatically make the complete drive a Class II product. Assess whether the marketed product itself is the qualifying component and meets the technical description/AVA_VAN criteria. |

### 2.2 Conformity assessment route (only after classification)

| Product status | CRA route |
|---|---|
| Ordinary product with digital elements, not Annex III/IV category | Article 32(1): manufacturer selects an available procedure, including Module A internal control, Module B+C, Module H, or an available/applicable European cybersecurity certification scheme. |
| Annex III Class I important product | Article 32(2): third-party assessment is required where the stated conditions apply, including absence/partial application of harmonised standards, common specifications or substantial-level certification scheme. |
| Annex III Class II important product | Article 32(3): Module B+C, Module H, or where available and applicable, a European cybersecurity certification scheme at assurance level at least substantial. |
| Annex IV critical product | Article 32(4) and Article 8; determine whether a delegated act requires certification or otherwise the applicable route. Do not assume a servo drive is Annex IV. |

**Important:** Article 24 is not the CRA conformity-assessment provision; it addresses open-source software stewards. The relevant conformity-assessment provision is Article 32.

## 3. Access-control compliance and design matrix

The legal anchor for access control is **Annex I Part I point 2(d)**. It requires protection from unauthorised access by appropriate control mechanisms, including but not limited to authentication, identity or access-management systems, and reporting on possible unauthorised access. The CRA does not prescribe one universal RBAC architecture or one specific password/certificate technology for every servo drive.

| Area | Legal basis / status | Recommended engineering control (risk-based) | Verification evidence |
|---|---|---|---|
| Authentication | Annex I Part I 2(d): explicit outcome/appropriate mechanism | Authenticate local, network, engineering-tool and service access according to threat model; avoid unauthenticated privileged operations | Interface inventory; authentication design; negative tests; access-control test report |
| Identity lifecycle | Annex I Part I 2(d): identity management is an example | Separate device, user, service and integration identities where relevant; define provisioning, rotation and revocation | Identity lifecycle procedure; credential provisioning records; revocation test |
| Role separation | Not a named universal CRA implementation requirement | Define operator, maintenance, commissioning and administrator roles if justified by functions and risk | Role-permission matrix; privilege escalation tests |
| Least privilege | Risk-based design principle; not separately named as a universal CRA clause | Grant only permissions needed for each role/service; isolate diagnostic/update functions | Threat model; permission review; unauthorized-action tests |
| Parameter protection | Annex I Part I 2(f) protects integrity of commands/programs/configuration from unauthorised modification | Authenticate and authorize sensitive configuration writes; protect parameter import/export and restore workflows | Parameter write authorization tests; integrity checks; audit evidence |
| Service/debug interfaces | Annex I Part I 2(j) requires attack-surface limitation, including external interfaces | Inventory USB, serial, JTAG/SWD, fieldbus and maintenance interfaces; disable/restrict unused interfaces where risk justifies | Interface inventory; production configuration; penetration test |
| Shared/default credentials | CRA does not state a universal clause requiring a particular unique-password scheme | Avoid universal shared credentials and undocumented backdoors; use per-device credentials or another proportionate mechanism | Credential uniqueness test; factory reset test; design review |
| Security event reporting | Annex I Part I 2(d) includes reporting possible unauthorised access | Record/report relevant access events where technically and proportionately appropriate; protect logs against tampering | Event catalogue; log integrity test; time/source attribution test |
| Secure remote maintenance | Derived from risk assessment and access-control requirements | Mutual authentication, scoped access, time-limited service sessions, customer authorization and session termination | Remote-service threat model; session tests; access revocation test |
| Recovery and factory reset | Risk-based; relevant to confidentiality/integrity and user instructions | Ensure reset/recovery does not restore insecure credentials or expose stored secrets | Reset/recovery test; secure erase procedure; post-reset security test |

### 3.1 Legal requirement vs implementation choice

- **Legal requirement:** appropriate protection from unauthorised access under Annex I Part I point 2(d), based on the product's risk assessment and applicability.
- **Potential implementation choices:** RBAC, least privilege, MFA, certificate-based authentication, unique per-device credentials, secure service mode, privileged-action confirmation, protected audit logs.
- These implementation choices should be selected and justified from the risk assessment; do not label each one a verbatim CRA mandate unless another applicable legal/standard requirement establishes it.
- Article 13(3) requires the risk assessment to indicate whether and how Annex I Part I point 2 requirements apply and how they are implemented. Where a requirement is not applicable, the technical documentation must contain a clear justification under Article 13(4).

## 4. Required evidence package

| Evidence ID | Deliverable | Minimum content |
|---|---|---|
| CL-01 | Product identity & intended-purpose statement | Product name/SKU, versions, market configuration, intended purpose, reasonably foreseeable use |
| CL-02 | Product-boundary diagram | Drive, option modules, firmware, engineering software, cloud/remote service, third-party components |
| CL-03 | Annex III classification record | Core-functionality rationale; each plausible category considered; Implementing Regulation 2025/2392 technical-description comparison |
| CL-04 | CRA applicability / other-law matrix | Applicable CRA requirements and relevant other Union legislation; reasoned exclusions |
| AC-01 | Interface and asset inventory | Ethernet/fieldbus, USB/serial, service/debug, parameter/configuration, update, diagnostics, identity stores |
| AC-02 | Threat and access-control model | Threat actors, assets, trust boundaries, attack paths, risk rating, selected mitigations |
| AC-03 | Role/permission matrix | Roles, protected operations, authorization policy, privilege boundaries |
| AC-04 | Security verification report | Authentication, authorization, privilege escalation, reset, service access, parameter integrity and event reporting tests |
| TD-01 | CRA technical documentation traceability | Article 13 risk assessment, Annex VII architecture, applied requirements, justification of non-applicability, test reports |

## 5. Open inputs — product-specific determination blocked

The following information is required before a product-specific classification or compliance conclusion can be issued:
- Exact product family and SKU(s), including network/communication option variants.
- Datasheet, installation/user manual, firmware/software architecture and marketed intended purpose.
- Whether drive, engineering tool, option module and remote service are separate products or one product boundary.
- Core functionality statement and any security product functionality that might match Annex III.
- Network, service and debug interface list; authentication/authorization model; credential lifecycle.
- Expected use/support period and EU market placement model.

Until these are supplied and reviewed, the product classification and the actual adequacy of access-control implementation remain **UNVERIFIED**.

## 6. Primary official sources

1. Regulation (EU) 2024/2847, especially Articles 7, 13, 28, 30–32, 64; Annex I Part I points 2(d), 2(f), 2(j); Annex III; Annex VII and VIII: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32024R2847
2. Commission Implementing Regulation (EU) 2025/2392, especially recitals (3)–(6), Article 2 and Annex I Class I/Class II technical descriptions: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R2392

## 7. Change history

- 2026-11-13 v0.1: Initial matrix created from the #43–#47 archive audit and official EUR-Lex texts. Product-specific applicability intentionally left UNVERIFIED.
