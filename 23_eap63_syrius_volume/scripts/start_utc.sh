docker run -d --name syr_utc --link syr_app:syrnet -p 42703:42703 \
--volume /Users/stefan/Documents/docker/syrdock/23_eap63_syrius_volume/syrius/properties:/opt/jboss/syrius/properties:ro \
--volume /Users/stefan/Documents/docker/syrdock/23_eap63_syrius_volume/syrius/config:/opt/jboss/syrius/config:ro \
--volume /Users/stefan/Documents/docker/syrdock/23_eap63_syrius_volume/syrius/logs:/opt/jboss/syrius/logs \
--volume /Users/stefan/Documents/docker/syrdock/23_eap63_syrius_volume/syrius/software/Executables/ASE-UTC-Server:/opt/jboss/syrius/ASE-UTC-Server/:ro \
clou/syr:3_06_HEAD_vol /opt/jboss/syrius/bin/utc_start
