
# Change this line to read the version from your file
$RELEASE_VERSION = Get-Content -Path C:\Users\Adrie\Documents\Programmation_Git\OfficeAssistant\PS\file.txt
# echo "RELEASE_VERSION=$RELEASE_VERSION" >> $env:GITHUB_ENV
echo "RELEASE_VERSION=$RELEASE_VERSION" 

$versionRegex = '.*v(\d+\.\d+\.\d+)$'

# $matches = $env:RELEASE_VERSION -match $versionRegex


if ($RELEASE_VERSION -match $versionRegex) {
$extractedVersion = $matches[1]
# echo "EXTRACTED_VERSION=$extractedVersion" >> $env:GITHUB_ENV
$EXTRACTED_VERSION=$extractedVersion
} else {
# $EXTRACTED_VERSION="000000000000" >> $env:GITHUB_ENV
 $EXTRACTED_VERSION="000000000000"
}

echo "Extracted Version: {$EXTRACTED_VERSION }"
echo "Ma variable test : $EXTRACTED_VERSION"
