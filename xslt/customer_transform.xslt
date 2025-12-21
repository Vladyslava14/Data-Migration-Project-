<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:output method="xml" indent="yes"/>

    <!-- Root -->
    <xsl:template match="/customers">
        <customers>
            <xsl:apply-templates select="customer"/>
        </customers>
    </xsl:template>

    <xsl:template match="customer">
        <customer>

            <!-- FIRST NAME -->
            <first_name>
                <xsl:choose>
                    <xsl:when test="contains(full_name, ' ')">
                        <xsl:value-of select="substring-before(full_name, ' ')"/>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:value-of select="full_name"/>
                    </xsl:otherwise>
                </xsl:choose>
            </first_name>

            <!-- LAST NAME -->
            <last_name>
                <xsl:choose>
                    <xsl:when test="contains(full_name, ' ')">
                        <xsl:value-of select="substring-after(full_name, ' ')"/>
                    </xsl:when>
                    <xsl:otherwise/>
                </xsl:choose>
            </last_name>

            <!-- BIRTHDATE (просто копіюємо як є) -->
            <birthdate>
                <xsl:value-of select="birthdate"/>
            </birthdate>

            <!-- STREET -->
            <street>
                <xsl:choose>
                    <xsl:when test="contains(address, ',')">
                        <xsl:value-of select="substring-before(address, ',')"/>
                    </xsl:when>
                    <xsl:otherwise/>
                </xsl:choose>
            </street>

            <!-- CITY -->
            <city>
                <xsl:choose>
                    <xsl:when test="contains(address, ',')">
                        <xsl:value-of select="normalize-space(substring-after(address, ','))"/>
                    </xsl:when>
                    <xsl:otherwise/>
                </xsl:choose>
            </city>

            <!-- PHONE -->
            <phone>
                <xsl:value-of select="phone"/>
            </phone>

            <!-- CREATED_AT -->
            <created_at>
                <xsl:value-of select="created_at"/>
            </created_at>

        </customer>
    </xsl:template>

</xsl:stylesheet>
