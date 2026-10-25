# Sources and interpretation

Primary references consulted on 2026-10-25 while developing this workflow. Follow the applicable version and organizational/domain requirements when using them; refresh changeable guidance before making version-specific or compliance claims.

- [NIST Secure Software Development Framework](https://csrc.nist.gov/projects/ssdf): lifecycle security practices, preparation, protection, secure development, and vulnerability response. The skill's G0–G7 identifiers, L/M/H tiers, and status vocabulary are local operating conventions, not NIST terminology or a compliance mapping.
- [NIST DevSecOps SSDF analysis](https://pages.nist.gov/nccoe-devsecops/appendix-c.html): illustrates applying security requirements, roles, and checks. The page itself describes its analysis as illustrative rather than a normative extension of SSDF.
- [OWASP Web Security Testing Guide, stable framework](https://owasp.github.io/www-project-web-security-testing-guide/stable/3-The_OWASP_Testing_Framework/): security testing activities across the lifecycle. Use relevant methods, not every test indiscriminately.
- [OWASP ASVS](https://asvs.owasp.org/): concrete security verification requirements for web applications/services. Choose and document applicable version and rigor; do not treat a tool scan as full ASVS verification.
- [DORA continuous delivery](https://dora.dev/capabilities/continuous-delivery/): small increments, continuous integration/testing, delivery automation, and feedback. This workflow does not prescribe a fixed organizational model.
- [Google SRE: Canarying Releases](https://sre.google/workbook/canarying-releases/): release identity, bounded rollout, representative exposure, and observed production signals. A canary cannot establish behavior outside its sample and conditions.
- [Google SRE: Monitoring](https://sre.google/workbook/monitoring/): service health, diagnosis, and useful monitoring. Infrastructure success alone does not demonstrate business correctness.
- [PIT mutation testing](https://pitest.org/): mutation mechanics and the limitation of execution coverage as evidence of fault detection. The skill does not adopt marketing claims or use mutation score as proof of overall quality.
- [W3C WCAG overview](https://www.w3.org/WAI/standards-guidelines/wcag/): web accessibility reference. Automated checks alone do not establish the usability of a complete journey.

The workflow, templates, visual guide, and illustrative examples are a synthesis. They do not certify security, regulatory compliance, production readiness, or correctness. Domain-specific requirements remain authoritative. No particular vendor, testing tool, browser, agent framework, or hosting service is required.
