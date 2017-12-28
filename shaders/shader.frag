

uniform vec3 diffuseColor;
uniform vec3 ambientColor;

in float intensity;

void main() 
{   
    gl_FragColor = vec4(max(diffuseColor * intensity, ambientColor), 1); 
}