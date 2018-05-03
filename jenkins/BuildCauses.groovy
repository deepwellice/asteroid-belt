def PrintBuildCauses() {
    def causes = currentBuild.rawBuild.getCauses()
    String causestring = 'The causes of this build:\n'
    causes.each { cause ->
        cause.properties.each { property ->
            causestring += "${property.key}: ${property.value}\n"
        }
        causestring += '-------------------------'
    }
    println causestring
}
