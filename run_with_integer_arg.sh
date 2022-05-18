
#!/bin/bash

die () {
	    echo >&2 "$@"
	        exit 1
	}

[ "$#" -eq 1 ] || die "1 argument required, $# provided"
echo $1 | grep -E -q '^[0-9]+$' || die "Numeric argument required, $1 provided"

night=$1
echo "NIGHT to work on: ${night}"
echo ""

sleep 0.5
python3 my_script.py "/path_to_somewhere/${night}" 2>&1 | tee "gen_${night}.log"

echo "Finished on $(date)"
