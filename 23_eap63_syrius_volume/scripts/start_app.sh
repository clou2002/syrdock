docker run -d --name syr_app \
--volume /Users/stefan/Documents/docker/syrdock/23_eap63_syrius_volume/syrius/properties:/opt/jboss/syrius/properties:ro \
--volume /Users/stefan/Documents/docker/syrdock/23_eap63_syrius_volume/syrius/config:/opt/jboss/syrius/config:ro \
--volume /Users/stefan/Documents/docker/syrdock/23_eap63_syrius_volume/syrius/config/standalone-full-syrius.xml:/opt/jboss/jboss-eap-6.3/standalone/configuration/standalone-full-syrius.xml:ro \
--volume /Users/stefan/Documents/docker/syrdock/23_eap63_syrius_volume/syrius/logs:/opt/jboss/syrius/logs \
--volume /Users/stefan/Documents/docker/syrdock/23_eap63_syrius_volume/syrius/software/Executables/ASE-J2EE-Server/ear/syrius_services.ear:/opt/jboss/jboss-eap-6.3/standalone/deployments/syrius_services.ear:ro \
--volume /Users/stefan/Documents/docker/syrdock/23_eap63_syrius_volume/syrius/software/Executables/ASE-UTC-Server:/opt/jboss/syrius/ASE-UTC-SERVER/:ro \
-p 42705:42705 -p 42707:42707 -p 9990:9990 clou/syr:3_06_HEAD_vol
