

in vec3 fragDiffuse;;
in float intensity;

void main() 
{   
    vec3 ambientColor = 0.2 * fragDiffuse;
    gl_FragColor = vec4(max(fragDiffuse * intensity, ambientColor), 1); 
}