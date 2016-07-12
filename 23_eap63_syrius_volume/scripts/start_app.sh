docker run -d --name syr_app \
--volume /c/Users/SSaupe/docker-workspace/ssa/syrdock/23_eap63_syrius_volume/syrius:/opt/jboss/syrius:ro \
--volume /c/Users/SSaupe/docker-workspace/ssa/syrdock/23_eap63_syrius_volume/syrius/logs:/opt/jboss/syrius/logs \
--volume /c/Users/SSaupe/docker-workspace/ssa/syrdock/23_eap63_syrius_volume/syrius/software/Executables/ASE-J2EE-Server/ear:/opt/jboss/jboss-eap-6.3/standalone/deployments:ro \
-p 42705:42705 -p 42707:42707 -p 9990:9990 clou/syr:3_06_HEAD_vol
